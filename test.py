from __future__ import annotations
from typing import TYPE_CHECKING, Callable
from ctypes import _Pointer
from ctypes import *
from ctypes.util import find_library
import sys

# helper code included by autoctypes


def _actp_libload(libname):
    if sys.platform in ["linux", "darwin"]:
        return CDLL(libname)
    if sys.platform == "win32":
        return CDLL(find_library(f"{libname.split('.')[0]}.dll"))
    raise RuntimeError(f"unsupported OS: {sys.platform}")


# file inline_test.h, line 1, column 12


def add_const(*args) -> int:
    return c_int32(c_int32(2).value + c_int32(3).value).value


# file inline_test.h, line 5, column 12


def mixed_const(*args) -> int:
    return c_int32(
        c_int32(10).value - c_int32(c_int32(4).value * c_int32(2).value).value
    ).value


# file inline_test.h, line 9, column 12


def nested_const(*args) -> int:
    return c_int32(
        c_int32(c_int32(1).value + c_int32(2).value).value
        * c_int32(c_int32(3).value + c_int32(4).value).value
    ).value


# file inline_test.h, line 12, column 14


def float_const(*args) -> float:
    return c_double(c_double(3.0).value + c_double(2.5).value).value


# file inline_test.h, line 16, column 14


def float_mix(*args) -> float:
    return c_double(
        c_double(c_double(1.5).value * c_double(2.0).value).value + c_double(4.5).value
    ).value


# file inline_test.h, line 19, column 12


def const_less(*args) -> int:
    return c_int32(c_int32(2).value < c_int32(3).value).value


# file inline_test.h, line 23, column 12


def const_equal(*args) -> int:
    return c_int32(c_int32(5).value == c_int32(5).value).value


# file inline_test.h, line 27, column 12


def const_not_equal(*args) -> int:
    return c_int32(c_int32(7).value != c_int32(8).value).value


# file inline_test.h, line 30, column 12


def const_and(*args) -> int:
    return c_int32(
        c_int32(c_int32(1).value < c_int32(2).value).value
        and c_int32(c_int32(3).value < c_int32(4).value).value
    ).value


# file inline_test.h, line 34, column 12


def const_or(*args) -> int:
    return c_int32(
        c_int32(c_int32(1).value > c_int32(2).value).value
        or c_int32(c_int32(3).value < c_int32(4).value).value
    ).value


# file inline_test.h, line 37, column 12


def const_bit_and(*args) -> int:
    return c_int32(c_int32(6).value & c_int32(3).value).value


# file inline_test.h, line 41, column 12


def const_bit_or(*args) -> int:
    return c_int32(c_int32(4).value | c_int32(1).value).value


# file inline_test.h, line 45, column 12


def const_bit_xor(*args) -> int:
    return c_int32(c_int32(5).value ^ c_int32(2).value).value


# file inline_test.h, line 49, column 12


def const_shift_left(*args) -> int:
    return c_int32(c_int32(1).value << c_int32(3).value).value


# file inline_test.h, line 53, column 12


def const_shift_right(*args) -> int:
    return c_int32(c_int32(8).value >> c_int32(2).value).value


# file inline_test.h, line 56, column 12


def const_int(*args) -> int:
    return c_int32(42).value


# file inline_test.h, line 60, column 14


def const_float(*args) -> float:
    return c_double(3.14).value


# file inline_test.h, line 64, column 13


def const_char(*args) -> bytes:
    return c_int32(90).value


# file inline_test.h, line 68, column 20


def const_string(*args) -> bytes:
    return c_char_p(b"hello world").value


# file inline_test.h, line 71, column 13


def ptr_add_const(*args) -> _Pointer[c_int32]:
    pass  # FIXME: generator raised StopIteration


# file inline_test.h, line 75, column 13


def ptr_sub_const(*args) -> _Pointer[c_int32]:
    pass  # FIXME: generator raised StopIteration


# file inline_test.h, line 78, column 12


def deep_expr(*args) -> int:
    return c_int32(
        c_int32(
            c_int32(c_int32(1).value + c_int32(2).value).value
            * c_int32(c_int32(3).value + c_int32(4).value).value
        ).value
        - c_int32(c_int32(5).value << c_int32(1).value).value
    ).value


# file inline_test.h, line 81, column 12


def chained_cmp(*args) -> int:
    return c_int32(
        c_int32(c_int32(1).value < c_int32(2).value).value
        == c_int32(c_int32(3).value < c_int32(4).value).value
    ).value
