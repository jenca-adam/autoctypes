from __future__ import annotations
from typing import TYPE_CHECKING, Callable
from ctypes import _Pointer
from ctypes import *
from ctypes.util import find_library
import sys
# helper code included by autoctypes

def _actp_libload(libname):
    if sys.platform in ['linux', 'darwin']:
        return CDLL(libname)
    if sys.platform == 'win32':
        return CDLL(find_library(f"{libname.split('.')[0]}.dll"))
    raise RuntimeError(f'unsupported OS: {sys.platform}')

libc = _actp_libload('libc.so.6')

# file declref_test.h, line 2, column 12

def idk(b: int) -> int:
    return c_int32(c_int32(b).value + c_int32(1).value).value
# file declref_test.h, line 5, column 12

def twice(a: int) -> int:
    return c_int32(c_int32(a).value * c_int32(2).value).value
# file declref_test.h, line 6, column 12

def mult(a: int, b: int) -> int:
    return c_int32(c_int32(a).value * c_int32(b).value).value
# file declref_test.h, line 7, column 12

def apply1(a: int) -> int:
    return c_int32(idk(c_int32(a).value)).value
# file /usr/include/stdio.h, line 370, column 12
if TYPE_CHECKING:
    libc.printf: Callable[[bytes], int]
libc.printf.argtypes = [c_char_p]
libc.printf.restype = c_int32

def printf(__format: bytes, *args) -> int:
    return libc.printf(__format, *args)
# file declref_test.h, line 10, column 13

def prInt(in_: int) -> None:
    c_int32(printf(c_char_p(b'The value is: ').value))
    c_int32(printf(c_char_p(b'%d\n').value, c_int32(in_).value))
# file declref_test.h, line 14, column 12

def apply2(in_: int, func: Callable[[int], int]) -> int:
    return c_int32(func(c_int32(in_).value)).value
# file declref_test.h, line 15, column 12

def func_cast(a: int, func: c_void_p) -> int:
    pass #FIXME: generator raised StopIteration
