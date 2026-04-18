import re
import keyword
import ctypes
from .clang_ext import is_function_inlined as is_function_inlined


def make_identifier(s):
    from . import ctypes_ext  # postpone import

    ident = re.sub(r"\W", "_", s)
    while keyword.iskeyword(ident) or hasattr(
        ctypes_ext, ident
    ):  # don't allow overwriting of c types!
        ident = ident + "_"  # potential name clash?
    return ident


def get_root_type(tp):
    if not getattr(tp, "_NEEDSDEF", None):
        return None
    while getattr(tp, "_NEEDSDEF", True) != True:
        tp = tp._NEEDSDEF
    if not hasattr(tp, "_NEEDSDEF"):
        return None
    return tp


def get_cursor_tokens(cursor):
    """
    https://github.com/llvm/llvm-project/issues/68340
    """
    tu = cursor.translation_unit

    start = cursor.extent.start
    start = cindex.SourceLocation.from_position(
        tu, start.file, start.line, start.column
    )

    end = cursor.extent.end
    end = cindex.SourceLocation.from_position(tu, end.file, end.line, end.column)

    extent = cindex.SourceRange.from_locations(start, end)

    yield from tu.get_tokens(extent=extent)
