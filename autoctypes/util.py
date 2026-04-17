import re
import keyword
from clang import cindex
import ctypes

if not hasattr(cindex.Cursor, "is_function_inlined"):
    cindex.conf.lib.clang_Cursor_isFunctionInlined.argtypes = [cindex.Cursor]
    cindex.conf.lib.clang_Cursor_isFunctionInlined.restype = ctypes.c_uint
    is_function_inlined = cindex.conf.lib.clang_Cursor_isFunctionInlined
else:
    is_function_inlined = cindex.Cursor.is_function_inlined

cindex.conf.lib.clang_getClangVersion.restype = ctypes.c_char_p
try:
    _clang_ver = cindex.conf.lib.clang_getClangVersion()
    _clang_ver_id = int(_clang_ver.split()[-1].split(b'.')[0])
    CLANG_INCLUDE_PATH = f"/usr/lib/clang/{_clang_ver_id}/include"
except:
    raise
    CLANG_INCLUDE_PATH = "/usr/include/clang"

def make_identifier(s):
    ident = re.sub(r"\W", "_", s)
    if keyword.iskeyword(ident):
        ident = ident + "_"  # potential name clash?
    return ident


def get_root_type(tp):
    if not getattr(tp, "_NEEDSDEF", None):
        return None
    while tp._NEEDSDEF != True:
        tp = tp._NEEDSDEF
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
