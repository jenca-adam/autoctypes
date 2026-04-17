import ctypes
import enum
from clang import cindex

if not hasattr(cindex.Cursor, "is_function_inlined"):
    cindex.conf.lib.clang_Cursor_isFunctionInlined.argtypes = [cindex.Cursor]
    cindex.conf.lib.clang_Cursor_isFunctionInlined.restype = ctypes.c_uint
    is_function_inlined = cindex.conf.lib.clang_Cursor_isFunctionInlined
else:
    is_function_inlined = cindex.Cursor.is_function_inlined

cindex.conf.lib.clang_getClangVersion.restype = ctypes.c_char_p
try:
    _clang_ver = cindex.conf.lib.clang_getClangVersion()
    _clang_ver_id = int(_clang_ver.split()[-1].split(b".")[0])
    CLANG_INCLUDE_PATH = f"/usr/lib/clang/{_clang_ver_id}/include"
except:
    CLANG_INCLUDE_PATH = "/usr/include/clang"


class EvalResultKind(enum.IntEnum):
    Int = 1
    Float = 2
    ObjCStrLiteral = 3
    StrLiteral = 4
    CFStr = 5
    Other = 6
    UnExposed = 0


cindex.conf.lib.clang_Cursor_Evaluate.argtypes = [cindex.Cursor]
cindex.conf.lib.clang_Cursor_Evaluate.restype = ctypes.c_void_p
cindex.conf.lib.clang_EvalResult_getKind.argtypes = [ctypes.c_void_p]
cindex.conf.lib.clang_EvalResult_getKind.restype = ctypes.c_int
cindex.conf.lib.clang_EvalResult_dispose.argtypes = [ctypes.c_void_p]
cindex.conf.lib.clang_EvalResult_getAsLongLong.restype = ctypes.c_longlong
cindex.conf.lib.clang_EvalResult_getAsLongLong.argtypes = [ctypes.c_void_p]
cindex.conf.lib.clang_EvalResult_getAsInt.restype = ctypes.c_int
cindex.conf.lib.clang_EvalResult_getAsInt.argtypes = [ctypes.c_void_p]
cindex.conf.lib.clang_EvalResult_getAsUnsigned.restype = ctypes.c_uint
cindex.conf.lib.clang_EvalResult_getAsUnsigned.argtypes = [ctypes.c_void_p]
cindex.conf.lib.clang_EvalResult_getAsDouble.restype = ctypes.c_double
cindex.conf.lib.clang_EvalResult_getAsDouble.argtypes = [ctypes.c_void_p]
cindex.conf.lib.clang_EvalResult_getAsStr.restype = ctypes.c_char_p
cindex.conf.lib.clang_EvalResult_getAsStr.argtypes = [ctypes.c_void_p]


class EvalResult(ctypes.Structure):
    def __init__(self, cursor):
        self.ptr = cindex.conf.lib.clang_Cursor_Evaluate(cursor)
        self.cursor = cursor

    @property
    def kind(self):
        return EvalResultKind(cindex.conf.lib.clang_EvalResult_getKind(self.ptr))

    def _get_as_longlong(self):
        return cindex.conf.lib.clang_EvalResult_getAsLongLong(self.ptr)

    def _get_as_double(self):
        return cindex.conf.lib.clang_EvalResult_getAsDouble(self.ptr)

    def _get_as_str(self):
        return cindex.conf.lib.clang_EvalResult_getAsStr(self.ptr)

    def _get_as_imag(self):
        return 1j * self._get_as_longlong()

    @property
    def value(self):
        handlers = {
            cindex.CursorKind.INTEGER_LITERAL: self._get_as_longlong,
            cindex.CursorKind.CHARACTER_LITERAL: self._get_as_longlong,
            cindex.CursorKind.IMAGINARY_LITERAL: self._get_as_imag,
            cindex.CursorKind.FLOATING_LITERAL: self._get_as_double,
            cindex.CursorKind.STRING_LITERAL: self._get_as_str,
        }
        if self.cursor.kind not in handlers:
            raise NotImplementedError(f"can't evaluate {self.cursor.kind}")
        return handlers[self.cursor.kind]()

    def __del__(self):
        cindex.conf.lib.clang_EvalResult_dispose(self.ptr)
