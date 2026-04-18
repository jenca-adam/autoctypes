from clang import cindex
import ast
import traceback
import _ctypes
import ctypes

from . import reconstruct, ctypes_ext
from .clang_ext import EvalResult
from .util import get_root_type


class Translator:
    """
    Loosely(!) translates an inline function's code to Python.
    It's not 100% accurate. Enable using --translate-inline
    """

    def __init__(self, inline_func, context):
        self.inline_func = inline_func
        self.extractor = inline_func._extractor
        self.ctx = context
        self.body = []
        self.needsdef = set()
        self._needtypes = set()
        self._args = {
            orig: (new, ctp)
            for orig, new, ctp in zip(
                inline_func._orig_argnames, inline_func._argnames, inline_func._argtypes
            )
        }
        self._decls = {}

    def print_ast(self, node, indent=0):
        print(f"{' '*indent}{node.kind} {node.spelling!r}")
        for child in node.get_children():
            self.print_ast(child, indent + 1)

    def translate(self, node):
        handlers = {
            cindex.CursorKind.COMPOUND_STMT: self._ignore,
            cindex.CursorKind.PAREN_EXPR: self._ignore,
            cindex.CursorKind.RETURN_STMT: self._translate_return_stmt,
            cindex.CursorKind.CALL_EXPR: self._translate_call_expr,
            cindex.CursorKind.INTEGER_LITERAL: self._translate_literal,
            cindex.CursorKind.FLOATING_LITERAL: self._translate_literal,
            cindex.CursorKind.STRING_LITERAL: self._translate_string_literal,
            cindex.CursorKind.CHARACTER_LITERAL: self._translate_literal,
            cindex.CursorKind.UNEXPOSED_EXPR: self._ignore,
            cindex.CursorKind.BINARY_OPERATOR: self._translate_binary_operator,
            cindex.CursorKind.DECL_REF_EXPR: self._translate_decl_ref,
        }
        handler = handlers.get(node.kind)
        if not handler:
            return
        yield from handler(node)

    def _is_ptr(self, ctp):
        return (
            issubclass(ctp, _ctypes.CFuncPtr)
            or issubclass(ctp, ctypes._Pointer)
            or issubclass(ctp, ctypes_ext.EPOINTER)
            or ctp in (ctypes.c_char_p, ctypes.c_wchar_p)
        )

    def _force_type(self, ctp, value, explicit=False):
        if issubclass(ctp, ctypes_ext.ENOCAST) and not explicit:  #
            return value
        reconstructed = reconstruct.reconstruct_type(ctp)
        ### We need the type to be defined to be able to cast to it
        needs = get_root_type(ctp)
        if needs:
            self.needsdef.add(self.extractor._codegen.from_ctype(needs, self.ctx))
        return ast.Call(reconstructed, [value])

    def _value_for_op(self, ctp, py_ast):
        if self._is_ptr(ctp):
            ### operations on pointers are equivalent to operations on addresses
            ### cast to c_void_p
            return ast.Attribute(
                value=ast.Call(
                    func=ast.Name("cast"), args=[py_ast, ast.Name("c_void_p")]
                ),
                attr="value",
            )
        ### for everything else, value should suffice(?) NOTE: structs?
        return ast.Attribute(
            value=py_ast,
            attr="value",
        )
    def _value_for_arg(self, ctp, py_ast):
        return self._value_for_return(ctp, py_ast) #for now
    def _resolve_name(self, name, curs):
        ### FILTHY
        if name in self._args:
            nm, ctp =self._args[name]
            return ast.Name(nm), ctp
        if name in self.ctx._renamed:
            nm, ctp = self.ctx._renamed[name]
            return ast.Name(nm), ctp
        if curs.referenced:

            ctp = self.extractor.get_ctypes_type(curs=curs.referenced)
            if ctp not in self._needtypes:
                self.needsdef.add(self.extractor._codegen.from_ctype(ctp, self.ctx))
                self._needtypes.add(ctp)
            if issubclass(ctp, ctypes_ext.EFUNC) and not self.ctx.wrapper_funcs:
                lib = self.ctx.find_lib(ctp.__qualname__)
                if lib:
                    return (ast.Subscript(ast.Name(lib.id), ast.Constant(ctp.__qualname__)), ctp)
            return (ast.Name(ctp.__qualname__), ctp)
        raise ValueError(
            f"unknown name: {name}"
        )  # TODO functions, global variables, declarations, etc.

    def _value_for_return(self, ctp, py_ast):
        if (
            issubclass(ctp, ctypes._SimpleCData)
            and hasattr(ctp, "value")
            or issubclass(ctp, ctypes_ext.EFORCE)
        ):  ## ALWAYS for forced-size integers
            return ast.Attribute(value=py_ast, attr="value")
        return py_ast

    def _ignore(self, node):
        # just chain it together
        for child in node.get_children():
            yield from self.translate(child)

    def _translate_return_stmt(self, node):
        kids = list(node.get_children())
        if not kids:
            yield ast.Return()
        try:
            result = next(self.translate(kids[0]))
            result_ctp = self.extractor.get_ctypes_type(curs=kids[0])
            yield ast.Return(value=self._value_for_return(result_ctp, result))
        except StopIteration:
            yield ast.Return()

    def _get_pointee(self, ctp):
        if not self._is_ptr(ctp) or ctp == ctypes.c_void_p:
            raise ValueError(f"attempted to get pointee of {ctp}")
        pointees = {
            ctypes.c_char_p: ctypes.c_char,
            ctypes.c_wchar_p: ctypes.c_wchar,
        }
        if ctp in pointees:
            return pointees[ctp]
        return ctp._type_

    def _pointer_arith_fix(self, left, right, left_tp, right_tp):
        """
        ONLY handles the PTR[op]VAL case
        """

        def mul_by_sizeof(ptr, val):
            return ast.BinOp(
                left=val,
                op=ast.Mult(),
                right=ast.Call(
                    func=ast.Name("sizeof"),
                    args=[reconstruct.reconstruct_type(self._get_pointee(ptr))],
                ),
            )

        left_is_ptr = self._is_ptr(left_tp)
        right_is_ptr = self._is_ptr(right_tp)
        if left_is_ptr and not right_is_ptr:
            right = mul_by_sizeof(left_tp, right)
        elif right_is_ptr and not left_is_ptr:
            left = mul_by_sizeof(right_tp, left)
        return left, right

    def _binop_binop(self, left, right, binop, left_ctp, right_ctp):
        ops = {
            cindex.BinaryOperator.Mul: ast.Mult,
            cindex.BinaryOperator.Div: ast.Div,
            cindex.BinaryOperator.Rem: ast.Mod,
            cindex.BinaryOperator.Add: ast.Add,
            cindex.BinaryOperator.Sub: ast.Sub,
            cindex.BinaryOperator.Shl: ast.LShift,
            cindex.BinaryOperator.Shr: ast.RShift,
            cindex.BinaryOperator.And: ast.BitAnd,
            cindex.BinaryOperator.Xor: ast.BitXor,
            cindex.BinaryOperator.Or: ast.BitOr,
        }
        if binop not in ops:
            return

        ### POINTER ARITHMETICS:
        ### 1) PTR [op] VAL => PTR [op] VAL*sizeof(PTR._type_)
        ### 2) PTR [op] PTR => (PTR [op] PTR)//sizeof(PTR._type_)
        ### we're assuming that the C code is valid

        left, right = self._pointer_arith_fix(left, right, left_ctp, right_ctp)
        result = ast.BinOp(left=left, op=ops[binop](), right=right)
        if self._is_ptr(left_ctp) and self._is_ptr(right_ctp):
            result = ast.BinOp(
                left=result,
                op=ast.FloorDiv(),
                right=ast.Call(
                    func=ast.Name("sizeof"),
                    args=[reconstruct.reconstruct_type(self._get_pointee(left_ctp))],
                ),
            )  # since they both have the same sizes, it doesn't matter which one we pick
        return result

    def _binop_cmp(self, left, right, binop):
        ops = {
            cindex.BinaryOperator.LT: ast.Lt,
            cindex.BinaryOperator.GT: ast.Gt,
            cindex.BinaryOperator.LE: ast.LtE,
            cindex.BinaryOperator.GE: ast.GtE,
            cindex.BinaryOperator.EQ: ast.Eq,
            cindex.BinaryOperator.NE: ast.NotEq,
        }
        if binop not in ops:
            return
        return ast.Compare(left=left, ops=[ops[binop]()], comparators=[right])

    def _binop_bool(self, left, right, binop):
        ops = {
            cindex.BinaryOperator.LAnd: ast.And,
            cindex.BinaryOperator.LOr: ast.Or,
        }
        if binop not in ops:
            return
        return ast.BoolOp(op=ops[binop](), values=[left, right])

    def _binop_augassign(self, left, right, binop):
        ops = {
            cindex.BinaryOperator.MulAssign: ast.Mult,
            cindex.BinaryOperator.DivAssign: ast.Div,
            cindex.BinaryOperator.RemAssign: ast.Mod,
            cindex.BinaryOperator.AddAssign: ast.Add,
            cindex.BinaryOperator.SubAssign: ast.Sub,
            cindex.BinaryOperator.ShlAssign: ast.LShift,
            cindex.BinaryOperator.ShrAssign: ast.RShift,
            cindex.BinaryOperator.AndAssign: ast.BitAnd,
            cindex.BinaryOperator.XorAssign: ast.BitXor,
            cindex.BinaryOperator.OrAssign: ast.BitOr,
        }
        if binop not in ops:
            return
        return ast.AugAssign(target=left, op=ops[binop](), value=right)

    def _binop_namedexpr(self, left, right, binop):
        if binop != cindex.BinaryOperator.Assign:
            return
        return ast.NamedExpr(target=left, value=right)

    def _translate_binary_operator(self, node):
        left_curs, right_curs, *_ = node.get_children()
        left_ctp = self.extractor.get_ctypes_type(curs=left_curs)
        right_ctp = self.extractor.get_ctypes_type(curs=right_curs)
        left_ast = next(self.translate(left_curs))
        right_ast = next(self.translate(right_curs))
        left = self._value_for_op(left_ctp, left_ast)
        right = self._value_for_op(right_ctp, right_ast)
        result_ctp = self.extractor.get_ctypes_type(curs=node)
        binop = node.binary_operator
        result = (
            self._binop_binop(left, right, binop, left_ctp, right_ctp)
            or self._binop_cmp(left, right, binop)
            or self._binop_bool(left, right, binop)
            or self._binop_augassign(left, right, binop, left_ctp, right_ctp)
        )
        if not result:
            raise NotImplementedError(binop)
        yield self._force_type(result_ctp, result)

    def _translate_literal(self, node):
        value = EvalResult(node).value
        ctp = self.extractor.get_ctypes_type(curs=node)
        reconstructed = reconstruct.reconstruct_type(ctp)
        yield ast.Call(reconstructed, args=[ast.Constant(value)])

    def _translate_string_literal(self, node):
        value = ast.literal_eval(node.spelling)  # careful with this
        yield self._force_type(ctypes.c_char_p, ast.Constant(value.encode("utf-8")))

    def _translate_call_expr(self, node):
        kids = list(node.get_children())
        if not kids:
            raise ValueError("empty CALL_EXPR")
        func = next(self.translate(kids[0]))
        restype = self.extractor.get_ctypes_type(curs=node)
        args = [
            self._value_for_arg(
                self.extractor.get_ctypes_type(curs=arg), next(self.translate(arg))
            )
            for arg in node.get_arguments()
        ]
        yield self._force_type(restype, ast.Call(func, args))

    def _translate_decl_ref(self, node):
        name, ctp = self._resolve_name(node.spelling, node)
        yield self._force_type(ctp, name)

    def get_py_ast(self):
        for node in self.inline_func._body:
            if node.kind != cindex.CursorKind.COMPOUND_STMT:
                continue
            self.print_ast(node)
            try:
                self.body.extend(
                    ast_node if isinstance(ast_node,ast.stmt) else ast.Expr(ast_node)
                    for ast_node in self.translate(node)
                )
            except Exception as e:
                traceback.print_exc()
                self.body = [ast.Pass(), ast.Name(f" #FIXME: {str(e)}")]
        try:
            ast.parse(
                ast.unparse(
                    ast.FunctionDef(
                        name="a", body=self.body, args=ast.arguments(), lineno=0
                    )
                )
            )
        except Exception as e:
            for node in self.body:
                print(ast.dump(node, indent=4))
            traceback.print_exc()
            self.body = [ast.Pass(), ast.Name(f" #FIXME: {str(e)}")]
        return self.body
