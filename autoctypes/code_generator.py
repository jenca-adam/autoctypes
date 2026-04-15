import ast
import warnings
import inspect
from .util import get_root_type
from .reconstruct import (
    reconstruct_code_generator,
    stringify_code_generator,
    reconstruct_type,
    reconstruct_type_hint,
)
from . import libload
from .ctypes_ext import *


class CodeGenerator:
    def reconstruct(self):
        return reconstruct_code_generator(self)

    def stringify(self):
        return stringify_code_generator(self)

    def __actp_code_generator__(self):
        raise NotImplementedError("abstract class")

    @classmethod
    def from_ctype(cls, ctype, ctx, *args, **kwargs):
        if issubclass(ctype, ESTRUCT):
            return StructCodeGenerator(ctype, ctx, *args, **kwargs)
        if issubclass(ctype, EFUNC):  # i regret my earlier decisions :(
            return FuncCodeGenerator(ctype, ctx, *args, **kwargs)
        if issubclass(ctype, EELABORATED):
            return cls.from_ctype(ctype._original, ctx)
        warnings.warn(
            UserWarning(f"can't generate {ctype.__qualname__}, not including")
        )
        breakpoint()
        return DummyCodeGenerator(ctype, *args, **kwargs)


class CompositorCodeGenerator(CodeGenerator):
    def __init__(self, gen, ctx):
        self.ctx = ctx
        self.gen = gen

    def __actp_code_generator__(self):
        body = []
        for cg in self.gen:
            body.extend(reconstruct_code_generator(cg))
        return body


class DummyCodeGenerator(CodeGenerator):
    def __init__(
        self,
        ctype,
        *args,
        **kwargs,
    ):
        self.ctype = ctype

    def __actp_code_generator__(self, *args, **kwargs):
        return [
            ast.Name(
                f"\n#FIXME: couldn't generate: {self.ctype.__qualname__}. No generator found"
            )
        ]


class StructCodeGenerator(CodeGenerator):
    def __init__(self, cstruct, ctx):
        self.struct = cstruct
        self.ctx = ctx

    def _gen_type_hints(self, type_check_guard=True):
        hints = []
        for field in self.struct._fields_:
            field_name, field_type, *bw = field
            hints.append(
                ast.AnnAssign(
                    target=ast.Name(field_name),
                    annotation=reconstruct_type_hint(field_type),
                    value=0,
                    simple=1,
                )
            )
            if field_name in self.struct._anonymous_:
                hints.extend(
                    CodeGenerator.from_ctype(field_type, self.ctx)._gen_type_hints(
                        False
                    )
                )
        if not hints:
            hints.append(ast.Pass())
        if type_check_guard:
            return [ast.If(ast.Name("TYPE_CHECKING"), hints)]
        return hints

    def __actp_code_generator__(self, *args, comment_override=None, **kwargs):
        taken = self.ctx._taken_names if self.ctx._taken_names is not None else set()
        body = [
            reconstruct_code_generator(locdef, self.ctx)
            for locdef in self.struct._localdefs
            if getattr(getattr(locdef, "struct", None), "__qualname__", None)
            not in taken
        ]
        if self.struct.__qualname__ in taken:
            return body
        taken.add(self.struct.__qualname__)
        if not self.ctx.type_hints:
            class_body = [ast.Pass()]
        else:
            class_body = self._gen_type_hints()
        comment = comment_override if comment_override is not None else self.ctx.comment
        if comment:
            body.append(ast.Name(f"\n# {self.struct._loc}"))  # ugly hack
        body.append(
            ast.ClassDef(
                self.struct.__qualname__,
                bases=[ast.Name("Union" if self.struct._is_union else "Structure")],
                body=class_body,
            )
        )
        fields_assign_targets = [
            ast.Attribute(ast.Name(self.struct.__qualname__), "_fields_")
        ]
        fields_assign_elts = [
            ast.Tuple(
                [ast.Constant(fld[0]), reconstruct_type(fld[1])]
                + ([ast.Constant(fld[2])] if len(fld) > 2 else [])
            )
            for fld in self.struct._fields_
        ]
        fields_assign_value = ast.List(fields_assign_elts)
        fields_assign = ast.Assign(fields_assign_targets, fields_assign_value, lineno=0)
        if self.struct._align_val > 0:
            align_assign_targets = [
                ast.Attribute(ast.Name(self.struct.__qualname__), "_align_")
            ]
            align_assign = ast.Assign(
                align_assign_targets, ast.Constant(self.struct._align_), lineno=0
            )
            body.append(align_assign)
        if self.struct._anonymous_:
            anon_assign_targets = [
                ast.Attribute(ast.Name(self.struct.__qualname__), "_anonymous_")
            ]
            anon_assign_value = ast.Tuple(
                [ast.Constant(name) for name in self.struct._anonymous_]
            )
            anon_assign = ast.Assign(anon_assign_targets, anon_assign_value, lineno=0)
            body.append(anon_assign)
        body.append(fields_assign)

        return body


class FuncCodeGenerator(CodeGenerator):
    def __init__(self, func, ctx):
        self.func = func
        self.ctx = ctx

    def __actp_code_generator__(self, *args, comment_override=None, **kwargs):
        body = []
        lib = self.ctx.find_lib(self.func.__qualname__)
        if not lib:
            warnings.warn(
                UserWarning(
                    f"function {self.func.__qualname__} "
                    "not found in any of the provided libraries."
                    f"Types won't be assigned. (code_generator at {self.func._loc})"
                )
            )
            return [
                ast.Name(
                    f"\n#FIXME: couldn't generate {self.func.__qualname__}: not found in any libraries"
                )
            ]
        self.ctx._taken_names.add(self.func.__qualname__)
        for req_type in (*self.func._argtypes, self.func._restype):
            to_define = get_root_type(req_type)
            if to_define and to_define.__qualname__ not in self.ctx._taken_names:
                body.extend(
                    CodeGenerator.from_ctype(
                        to_define, self.ctx
                    ).__actp_code_generator__(*args, comment_override, **kwargs)
                )

        libid = lib.id
        comment = comment_override if comment_override is not None else self.ctx.comment
        if comment:
            body.append(ast.Name(f"\n# {self.func._loc}"))  # -||-
        if (
            self.func.__qualname__.isidentifier()
        ):  # use getattr for valid identifiers instead of getitem
            libfn = ast.Attribute(ast.Name(libid), self.func.__qualname__)
        else:
            libfn = ast.Subscript(ast.Name(libid), ast.Constant(self.func.__qualname__))

        if self.ctx.type_hints:
            hint = [
                ast.AnnAssign(
                    target=libfn,
                    annotation=reconstruct_type_hint(self.func),
                    value=0,
                    simple=1,
                )
            ]
            body.append(ast.If(ast.Name("TYPE_CHECKING"), hint))
        body.append(
            ast.Assign(
                [ast.Attribute(libfn, "argtypes")],
                ast.List(reconstruct_type(argtp) for argtp in self.func._argtypes),
                lineno=0,
            )
        )
        body.append(
            ast.Assign(
                [ast.Attribute(libfn, "restype")],
                reconstruct_type(self.func._restype),
                lineno=0,
            )
        )

        if self.ctx.wrapper_funcs:
            func_call_args = [
                *(ast.Name(argname) for argname in self.func._argnames),
                ast.Starred(ast.Name("args")),
            ]

            func_body = [ast.Return(ast.Call(libfn, args=func_call_args))]
            if self.ctx.type_hints:
                func_def_args = ast.arguments(
                    posonlyargs=[],
                    args=[
                        ast.arg(
                            arg=argname,
                            annotation=reconstruct_type_hint(argtype),
                            type_comment=None,
                        )
                        for (argname, argtype) in zip(
                            self.func._argnames, self.func._argtypes
                        )
                    ],
                    vararg=ast.arg("args"),
                )
                func_def_returns = reconstruct_type_hint(self.func._restype)
            else:
                func_def_args = ast.arguments(
                    posonlyargs=[],
                    args=[
                        ast.arg(arg=argname, annotation=None, type_comment=None)
                        for argname in self.func._argnames
                    ],
                    vararg=ast.arg("args"),
                )
                func_def_returns = None
            body.append(
                ast.FunctionDef(
                    name=self.func.__qualname__,
                    args=func_def_args,
                    body=func_body,
                    lineno=0,
                )
            )

        return body


class TypedefCodeGenerator(CodeGenerator):
    def __init__(self, ctype, name, ctx, loc="<unknown loc>"):
        self.ctype = ctype
        self.loc = loc
        self.ctx = ctx
        self.name = name

    def __actp_code_generator__(self, *args, comment_override=None, **kwargs):
        body = []
        to_define = get_root_type(self.ctype)
        if to_define and to_define.__qualname__ not in self.ctx._taken_names:
            body.extend(
                CodeGenerator.from_ctype(to_define, self.ctx).__actp_code_generator__(
                    *args, comment_override, **kwargs
                )
            )
        comment = comment_override if comment_override is not None else self.ctx.comment
        if comment:
            body.append(ast.Name(f"\n# {self.loc}"))
        body.append(
            ast.Assign([ast.Name(self.name)], reconstruct_type(self.ctype), lineno=0)
        )
        return body


class CoPyCodeGenerator(CodeGenerator):
    def __init__(self, obj, ctx, required=False):
        self.obj = obj
        self.ctx = ctx
        self.required = required
        self.ast = ast.parse(inspect.getsource(obj))

    def __actp_code_generator__(self, *args, comment_override=None, **kwargs):
        body = []
        if not self.required and not self.ctx.fluff:
            return body
        comment = comment_override if comment_override is not None else self.ctx.comment
        if comment:
            body.append(ast.Name("\n# helper code included by autoctypes"))
        body.append(self.ast)
        body.append(ast.Name("\n"))
        return body


class ImportCodeGenerator(CodeGenerator):
    def __init__(self, ctx):
        self.ctx = ctx

    def __actp_code_generator__(self, *args, comment_override=None, **kwargs):
        body = []
        comment = comment_override if comment_override is not None else self.ctx.comment
        if self.ctx.type_hints:
            body.append(ast.ImportFrom("__future__", [ast.alias("annotations")]))
            body.append(
                ast.ImportFrom(
                    "typing", [ast.alias("TYPE_CHECKING"), ast.alias("Callable")]
                )
            )
            body.append(ast.ImportFrom("ctypes", [ast.alias("_Pointer")]))
        body.append(ast.ImportFrom("ctypes", [ast.alias("*")]))
        body.append(ast.ImportFrom("ctypes.util", [ast.alias("find_library")]))
        body.append(ast.Import([ast.alias("sys")]))
        if self.ctx.fluff:
            body.append(ast.Import([ast.alias("struct")]))
        return body


class CtxSetupCodeGenerator(CodeGenerator):
    def __init__(self, ctx):
        self.ctx = ctx

    def __actp_code_generator__(self, *args, **kwargs):
        body = []
        body.extend(
            reconstruct_code_generator(
                CoPyCodeGenerator(libload._actp_libload, self.ctx, True)
            )
        )
        for lib in self.ctx.libs:
            body.append(
                ast.Assign(
                    [ast.Name(lib.id)],
                    ast.Call(ast.Name("_actp_libload"), [ast.Constant(lib.name)]),
                    lineno=0,
                )
            )
        return body
