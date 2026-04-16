"""
Code reconstruction utilities
"""

import ctypes
import ast
import inspect
import warnings

import _ctypes

CTYPE = ctypes.c_int.mro()[-2]
CTYPE_RESOLVE = {
    ctypes.c_byte: int,
    ctypes.c_short: int,
    ctypes.c_int: int,
    ctypes.c_long: int,
    ctypes.c_longlong: int,
    ctypes.c_ubyte: int,
    ctypes.c_ushort: int,
    ctypes.c_uint: int,
    ctypes.c_ulong: int,
    ctypes.c_ulonglong: int,
    ctypes.c_float: float,
    ctypes.c_double: float,
    ctypes.c_longdouble: float,
    ctypes.c_double_complex: complex,
    ctypes.c_longdouble_complex: complex,
    ctypes.c_char: bytes,
    ctypes.c_wchar: bytes,
    ctypes.c_char_p: bytes,
    ctypes.c_wchar_p: bytes,
    ctypes.c_void_p: ctypes.c_void_p,
}


def reconstruct_type(ctype):
    """
    Creates an AST from a ctypes type.
    """
    # pylint: disable=protected-access
    if ctype is None:
        return ast.Name(str(ctype))
    if hasattr(ctype, "__actp_reconstruct__"):
        return ctype.__actp_reconstruct__()
    ### FALLBACKS
    if not inspect.isclass(ctype) or not issubclass(ctype, CTYPE):
        raise TypeError(f"{ctype} is not a ctypes type")
    if ctypes.Array in ctype.mro():
        return ast.BinOp(
            reconstruct_type(ctype._type_), ast.Mult(), ast.Constant(ctype._length_)
        )
    if ctypes._Pointer in ctype.mro():
        return ast.Call(ast.Name("POINTER"), (reconstruct_type(ctype._type_),))
    if _ctypes.CFuncPtr in ctype.mro():
        return ast.Call(
            ast.Name("CFUNCTYPE"),
            (
                reconstruct_type(ctype._restype_),
                *(reconstruct_type(tp) for tp in ctype._argtypes_),
            ),
        )
    return ast.Name(ctype.__qualname__)


def reconstruct_type_hint(ctype, as_ctypes_type=False):
    """
    Creates a type hint AST from a ctypes type.
    """
    if ctype is None:
        return ast.Name("None")
    if hasattr(ctype, "__actp_type_hint__"):
        return ctype.__actp_type_hint__(as_ctypes_type)
    if ctype in CTYPE_RESOLVE and not as_ctypes_type:
        return ast.Name(CTYPE_RESOLVE[ctype].__name__)
    return ast.Name(ctype.__name__)


def stringify_type(ctype):
    """
    Creates a Python code representation of a ctypes type
    """
    return ast.unparse(reconstruct_type(ctype))


def reconstruct_code_generator(code_generator, *args, **kwargs):
    """
    Creates an AST from a definition.
    """
    if not hasattr(code_generator, "__actp_code_generator__"):
        breakpoint()
        raise TypeError("can't reconstruct: missing __actp_code_generator__")
    return code_generator.__actp_code_generator__(*args, **kwargs)


def stringify_code_generator(code_generator, *args, **kwargs):
    """
    Creates a Python code representation of a definition
    """
    mod = ast.Module(reconstruct_code_generator(code_generator, *args, **kwargs))
    return ast.unparse(mod)
