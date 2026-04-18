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


# file declref_test.h, line 1, column 12

def idk(b: int, *args) -> int:
    return c_int32(c_int32(b).value + c_int32(1).value).value
# file declref_test.h, line 4, column 12

def twice(a: int, *args) -> int:
    return c_int32(c_int32(a).value * c_int32(2).value).value
# file declref_test.h, line 5, column 12

def mult(a: int, b: int, *args) -> int:
    return c_int32(c_int32(a).value * c_int32(b).value).value
# file declref_test.h, line 6, column 12

def apply1(a: int, *args) -> int:
    pass #FIXME: unknown name: idk
# file declref_test.h, line 9, column 12

def apply2(in_: int, func: Callable[[int], int], *args) -> int:
    return c_int32(CFUNCTYPE(c_int32, c_int32)(func)(c_int32(in_))).value
# file declref_test.h, line 10, column 12

def func_cast(a: int, func: c_void_p, *args) -> int:
    pass #FIXME: generator raised StopIteration
