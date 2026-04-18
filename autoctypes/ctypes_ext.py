"""
Extended ctypes structures
"""

# pylint: disable=unused-wildcard-import, wildcard-import, invalid-name, too-few-public-methods

import struct
import sys
import ast
from ctypes import *
from .reconstruct import reconstruct_type, reconstruct_type_hint
from .util import make_identifier

### STRUCT (factory)


class ENOCAST:
    pass


class ESTRUCT:
    pass


class EFUNC(ENOCAST):
    pass


class EELABORATED:
    pass


class EPOINTER:
    pass


class EARRAY:
    pass


class EFORCE:
    pass


class EINLINE(ENOCAST):
    pass


### INLINE (factory)
def make_inline_func(
    name,
    restype,
    argtypes,
    argnames,
    orig_argnames,
    extractor,
    localdefs,
    variadic,
    body,
    locs,
    context,
):
    class _INLINE(EINLINE):
        __qualname__ = name
        __name__ = name
        _ctx = context
        _restype = restype
        _argtypes = argtypes
        _argnames = argnames
        _orig_argnames = orig_argnames
        _body = body
        _loc = locs
        _extractor = extractor
        _localdefs = localdefs
        _variadic = variadic
        _IS_INLINE = True

        @classmethod
        def __actp_reconstruct__(self):
            return ast.Name(name)

        @classmethod
        def __actp_type_hint__(self, as_ctypes_type=False):
            return ast.Subscript(
                ast.Name("Callable"),
                ast.Tuple(
                    (
                        ast.List(
                            [reconstruct_type_hint(argt) for argt in cls._argtypes]
                        ),
                        reconstruct_type_hint(cls._restype),
                    )
                ),
            )

    return _INLINE


### FORCE (factory)
def make_forced_type(name, type_hint):
    class _FORCE(EFORCE):
        __qualname__ = name
        __name__ = name

        @classmethod
        def __actp_reconstruct__(self):
            return ast.Name(name)

        @classmethod
        def __actp_type_hint__(self, as_ctypes_type=False):
            if as_ctypes_type:
                return self.__actp_reconstruct__()
            return reconstruct_type_hint(type_hint)

    return _FORCE


### STRUCT(factory)
def make_struct(name, fields, align, locs, localdefs, is_union, context, anon):
    """
    Creates a user-defined struct object.
    """

    class _STRUCT(ESTRUCT):
        _NEEDSDEF = True
        __qualname__ = name
        __name__ = name
        _ctx = context
        _loc = locs
        _localdefs = localdefs
        _is_union = is_union
        _align_val = align

        if align > 0:
            _align_ = align
        _anonymous_ = anon
        _fields_ = fields

        @classmethod
        def __actp_reconstruct__(self):
            return ast.Name(name)

        @classmethod
        def __actp_type_hint__(self, *args):
            return ast.Name(name)

    return _STRUCT


### FUNC(factory)
def make_func(name, restype, argtypes, argnames, localdefs, variadic, locs, context):
    """
    Creates an user-defined function object
    """

    class _FUNC(EFUNC):
        __name__ = name
        __qualname__ = name
        _argtypes = argtypes
        _argnames = argnames
        _restype = restype
        _ctx = context
        _variadic = variadic
        _localdefs = localdefs
        _loc = locs
        _IS_INLINE = False

        @classmethod
        def __actp_reconstruct__(cls):
            return ast.Call(
                ast.Name("CFUNCTYPE"),
                (
                    reconstruct_type(cls._restype),
                    *(reconstruct_type(argtp) for argtp in cls._argtypes),
                ),
            )

        @classmethod
        def __actp_type_hint__(cls, *args):
            return ast.Subscript(
                ast.Name("Callable"),
                ast.Tuple(
                    (
                        ast.List(
                            [reconstruct_type_hint(argt) for argt in cls._argtypes]
                        ),
                        reconstruct_type_hint(cls._restype),
                    )
                ),
            )

    return _FUNC


### ELABORATED (factory)


def mk_elaborated(raw_name, ctype):
    """
    Creates a representation of an elaborated object
    """
    name = make_identifier(raw_name.split()[-1].strip())

    class _ELABORATED(EELABORATED):
        __name__ = name
        __qualname__ = name
        _original = ctype

        @classmethod
        def __actp_reconstruct__(cls):
            return ast.Name(cls.__qualname__)

        @classmethod
        def __actp_type_hint__(cls, *args):
            return ast.Name(cls.__qualname__)

    return _ELABORATED


### POINTER (factory)


def mk_ptr(ctype):
    """
    Creates a representation of a pointer object
    """

    class _POINTER(EPOINTER):
        __pointee = ctype
        _type_ = ctype
        _NEEDSDEF = ctype if getattr(ctype, "_NEEDSDEF", False) else False

        @classmethod
        def __actp_reconstruct__(cls):
            if cls.__pointee in (None, type(None)):
                return ast.Name("c_void_p")
            return ast.Call(ast.Name("POINTER"), [reconstruct_type(cls.__pointee)])

        @classmethod
        def __actp_type_hint__(cls, *args):
            # is there a better way?
            if cls.__pointee in (None, type(None)):
                return ast.Name("c_void_p")
            return ast.Subscript(
                ast.Name("_Pointer"), reconstruct_type_hint(cls.__pointee, True)
            )

    return _POINTER


### ARRAY (factory)


def mk_array(ctype, array_size):
    """
    Creates a representation of an array object
    """

    class _ARRAY(EARRAY):
        __item_type = ctype
        __size = array_size
        _NEEDSDEF = ctype if getattr(ctype, "_NEEDSDEF", False) else False

        @classmethod
        def __actp_reconstruct__(cls):
            return ast.BinOp(
                reconstruct_type(cls.__item_type), ast.Mult(), ast.Constant(cls.__size)
            )

        @classmethod
        def __actp_type_hint__(cls, *args):
            return ast.Subscript(
                ast.Name("Array"), reconstruct_type_hint(cls.__item_type, True)
            )

    return _ARRAY


### COMPLEX (deprecated in favor of c_float_complex)


class c_complex(Structure):
    """
    Complex number
    """

    _fields_ = [("real", c_double), ("imag", c_double)]

    def __init__(self, num):
        self.real = num.real
        self.imag = num.imag

    @property
    def value(self):
        """
        Returns the value as a Python complex object
        """
        return self.real + 1j * self.imag


### FLOAT128


class c_float128(Structure):
    """
    Represents a quad precision float(128 bit).
    """

    _fields_ = [("lo", c_uint64), ("hi", c_uint64)]

    def __init__(self, num):
        packed = struct.pack("d", num)
        unpacked = struct.unpack("Q", packed)[0]
        sign = (unpacked >> 63) & 0x1
        exponent = (unpacked >> 52) & 0x7FF
        significand = (unpacked & 0xFFFFFFFFFFFFF) << 60  # weird endianness

        bias = 0x3FFF

        exp_128 = exponent - 1023 + bias
        if exponent == 0:
            exp_128 = 0
            significand <<= 1

        self.hi = (sign << 63) | (exp_128 << 48) | (significand >> 64)
        self.lo = significand & 0xFFFFFFFFFFFFFFFF

    @property
    def value(self):
        """
        Returns the value as a python float object.
        The value returned is double precision, as all Python floats.
        """
        bias = 0x3FFF
        exp = ((self.hi >> 48) & 0x7FFF) - bias
        sign_bit = self.hi >> 63
        significand = (self.hi & 0xFFFFFFFFFFFF) << 64 | self.lo  # 112 bits

        if significand == 0 and exp == -bias:  # special case
            return 0

        sign = -1 if sign_bit else 1
        if exp >= sys.float_info.max_exp:
            if significand:
                return float("nan")
            return sign * float("inf")

        return sign * (2**exp) * (1 + significand / 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFF)


### HALF


class c_half(Structure):
    """
    Represents a half precision float (16 bit)
    """

    _fields_ = [("i", c_ushort)]

    def __init__(self, num):
        packed = struct.pack("e", num)
        self.i = struct.unpack("H", packed)[0]

    @property
    def value(self):
        """
        Returns the value as a python float object.
        The value returned is double precision, as all Python floats.
        """

        packed = struct.pack("H", self.i)
        return struct.unpack("e", packed)[0]


### INT128


class c_int128(Structure):
    """
    Represents a 128bit signed integer
    """

    _fields_ = [("lo", c_uint64), ("hi", c_uint64)]
    _MAX = (1 << 63) - 1

    def __init__(self, num):
        sign_bit = 1 if num < 0 else 0
        unum = abs(num)
        if unum > self._MAX:
            raise OverflowError("int too large to convert to c_int128")
        self.lo = unum & 0xFFFFFFFFFFFFFFFF
        self.hi = (unum >> 64) | (sign_bit << 63)

    @property
    def value(self):
        """
        Returns the value as a Python int
        """
        sign_bit, uhi = self.hi >> 63, self.hi & 0x7FFFFFFFFFFFFFFF
        return (self.lo | (uhi << 64)) * (-1) ** sign_bit


### UINT128


class c_uint128(Structure):
    """
    Represents a 128bit unsigned integer.
    """

    _fields_ = [("lo", c_uint64), ("hi", c_uint64)]
    _MAX = (1 << 64) - 1

    def __init__(self, num):
        if num > self._MAX:
            raise OverflowError("int too large to convert to c_int128")
        self.lo = num & 0xFFFFFFFFFFFFFFFF
        self.hi = num >> 64

    @property
    def value(self):
        """
        Returns the value as a Python int
        """

        return self.lo | (self.hi << 64)


c_int16_FORCE = make_forced_type("c_int16", int)
c_uint16_FORCE = make_forced_type("c_uint16", int)
c_int32_FORCE = make_forced_type("c_int32", int)
c_uint32_FORCE = make_forced_type("c_uint32", int)
c_int64_FORCE = make_forced_type("c_int64", int)
c_uint64_FORCE = make_forced_type("c_uint64", int)
TYPE_EXTENSIONS = [c_float128, c_half, c_int128, c_uint128]
