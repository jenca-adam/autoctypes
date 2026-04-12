# pylint: disable=unused-wildcard-import, wildcard-import, invalid-name, too-few-public-methods, protected-access, unused-argument
import ast
import warnings
import inspect
from .reconstruct import (
    reconstruct_code_generator,
    stringify_code_generator,
    reconstruct_type,
    reconstruct_type_hint,
)
from .ctypes_ext import *


class CodeGenerator:
    def reconstruct(self):
        return reconstruct_code_generator(self)

    def stringify(self):
        return stringify_code_generator(self)

    def __actp_code_generator__(self):
        raise NotImplementedError("abstract class")

    @classmethod
    def from_ctype(cls, ctype, *args, **kwargs):
        if issubclass(ctype, ESTRUCT):
            return StructCodeGenerator(ctype, *args, **kwargs)
        if issubclass(ctype, EFUNC):  # i regret my earlier decisions :(
            return FuncCodeGenerator(ctype, *args, **kwargs)
        if issubclass(ctype, EELABORATED):
            return cls.from_ctype(ctype._original)
        warnings.warn(
            UserWarning(f"can't generate {ctype.__qualname__}, not including")
        )
        return DummyCodeGenerator(ctype, *args, **kwargs)


class DummyCodeGenerator(CodeGenerator):
    def __init__(
        self,
        ctype,
        *args,
        **kwargs,
    ):
        self.ctype = ctype

    def __actp_code_generator__(self, *args, **kwargs):
        return [ast.Name(f"\n#FIXME: couldn't generate: {self.ctype.__qualname__}")]


class StructCodeGenerator(CodeGenerator):
    def __init__(self, cstruct):
        self.struct = cstruct

    def _gen_type_hints(self, type_check_guard=True):
        hints = []
        for field in self.struct._fields_:
            field_name, field_type = field
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
                    CodeGenerator.from_ctype(field_type)._gen_type_hints(False)
                )
        if type_check_guard:
            return [ast.If(ast.Name("TYPE_CHECKING"), hints)]
        return hints

    def __actp_code_generator__(
        self, *args, taken=None, comment_override=None, type_hints=False, **kwargs
    ):
        taken = taken if taken is not None else set()
        body = [
            reconstruct_code_generator(locdef, taken=taken, type_hints=type_hints)
            for locdef in self.struct._localdefs
            if getattr(getattr(locdef, "struct", None), "__qualname__", None)
            not in taken
        ]
        if self.struct.__qualname__ in taken:
            return body
        taken.add(self.struct.__qualname__)
        if not type_hints:
            class_body = [ast.Pass()]
        else:
            class_body = self._gen_type_hints()
        comment = (
            comment_override
            if comment_override is not None
            else self.struct._ctx.comment
        )
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
                + ([ast.Const(fld[2])] if len(fld) > 2 else [])
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
    def __init__(self, func):
        self.func = func

    def __actp_code_generator__(self, *args, comment_override=None, **kwargs):
        lib = self.func._ctx.find_lib(self.func.__qualname__)
        if not lib:
            warnings.warn(
                UserWarning(
                    f"self.function {self.func.__qualname__}"
                    "not found in any of the provided libraries."
                    f"Types won't be assigned. (code_generator at {self.func._loc})"
                )
            )
            return ()
        libid = lib.id
        body = []
        comment = (
            comment_override if comment_override is not None else self.func._ctx.comment
        )
        if comment:
            body.append(ast.Name(f"\n# {self.func._loc}"))  # -||-
        if (
            self.func.__qualname__.isidentifier()
        ):  # use getattr for valid identifiers instead of getitem
            libfn = ast.Attribute(ast.Name(libid), self.func.__qualname__)
        else:
            libfn = ast.Subscript(ast.Name(libid), ast.Constant(self.func.__qualname__))
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

        return body


class TypedefCodeGenerator(CodeGenerator):
    def __init__(self, ctype, name, ctx, loc="<unknown loc>"):
        self.ctype = ctype
        self.loc = loc
        self.ctx = ctx
        self.name = name

    def __actp_code_generator__(self, *args, comment_override=None, **kwargs):
        body = []
        comment = comment_override if comment_override is not None else self.ctx.comment
        if comment:
            body.append(ast.Name(f"\n# {self.loc}"))
        body.append(
            ast.Assign([ast.Name(self.name)], reconstruct_type(self.ctype), lineno=0)
        )
        return body


class CoPyCodeGenerator(CodeGenerator):
    def __init__(self, cls, ctx):
        self.cls = cls
        self.ctx = ctx
        self.ast = ast.parse(inspect.getsource(cls))

    def __actp_code_generator__(self, *args, comment_override=None, **kwargs):
        body = []
        comment = comment_override if comment_override is not None else self.ctx.comment
        if comment:
            body.append(ast.Name("\n# helper code included by autoctypes"))
        body.append(self.ast)
        return body


class SetupCodeGenerator(CodeGenerator):
    def __init__(self, ctx):
        self.ctx = ctx

    def __actp_code_generator__(self, *args, comment_override=None, **kwargs):
        body = []
        comment = comment_override if comment_override is not None else self.ctx.comment
        body.append(ast.ImportFrom("ctypes", ast.alias("*")))
        body.append(ast.ImportFrom("ctypes.util", ast.alias("find_library")))


class CompositorCodeGenerator(CodeGenerator):
    def __init__(self, gen, ctx):
        self.ctx = ctx
        self.gen = gen

    def __actp_code_generator__(self):
        body = []
        for df in self.gen:
            body.extend(reconstruct_code_generator(body))
        return body
