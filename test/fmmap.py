
# file /usr/include/bits/types.h, line 31, column 23
__u_char = c_ubyte

# file /usr/include/bits/types.h, line 32, column 28
__u_short = c_ushort

# file /usr/include/bits/types.h, line 33, column 22
__u_int = c_uint

# file /usr/include/bits/types.h, line 34, column 27
__u_long = c_ulong

# file /usr/include/bits/types.h, line 37, column 21
__int8_t = c_byte

# file /usr/include/bits/types.h, line 38, column 23
__uint8_t = c_ubyte

# file /usr/include/bits/types.h, line 39, column 26
__int16_t = c_short

# file /usr/include/bits/types.h, line 40, column 28
__uint16_t = c_ushort

# file /usr/include/bits/types.h, line 41, column 20
__int32_t = c_int

# file /usr/include/bits/types.h, line 42, column 22
__uint32_t = c_uint

# file /usr/include/bits/types.h, line 44, column 25
__int64_t = c_long

# file /usr/include/bits/types.h, line 45, column 27
__uint64_t = c_ulong

# file /usr/include/bits/types.h, line 52, column 18
__int_least8_t = c_byte

# file /usr/include/bits/types.h, line 53, column 19
__uint_least8_t = c_ubyte

# file /usr/include/bits/types.h, line 54, column 19
__int_least16_t = c_short

# file /usr/include/bits/types.h, line 55, column 20
__uint_least16_t = c_ushort

# file /usr/include/bits/types.h, line 56, column 19
__int_least32_t = c_int

# file /usr/include/bits/types.h, line 57, column 20
__uint_least32_t = c_uint

# file /usr/include/bits/types.h, line 58, column 19
__int_least64_t = c_long

# file /usr/include/bits/types.h, line 59, column 20
__uint_least64_t = c_ulong

# file /usr/include/bits/types.h, line 63, column 18
__quad_t = c_long

# file /usr/include/bits/types.h, line 64, column 27
__u_quad_t = c_ulong

# file /usr/include/bits/types.h, line 72, column 18
__intmax_t = c_long

# file /usr/include/bits/types.h, line 73, column 27
__uintmax_t = c_ulong

# file /usr/include/bits/types.h, line 145, column 25
__dev_t = c_ulong

# file /usr/include/bits/types.h, line 146, column 25
__uid_t = c_uint

# file /usr/include/bits/types.h, line 147, column 25
__gid_t = c_uint

# file /usr/include/bits/types.h, line 148, column 25
__ino_t = c_ulong

# file /usr/include/bits/types.h, line 149, column 27
__ino64_t = c_ulong

# file /usr/include/bits/types.h, line 150, column 26
__mode_t = c_uint

# file /usr/include/bits/types.h, line 151, column 27
__nlink_t = c_ulong

# file /usr/include/bits/types.h, line 152, column 25
__off_t = c_long

# file /usr/include/bits/types.h, line 153, column 27
__off64_t = c_long

# file /usr/include/bits/types.h, line 154, column 25
__pid_t = c_int

# file /usr/include/bits/types.h, line 155, column 12

class __fsid_t(Structure):
    pass
__fsid_t._align_ = 4
__fsid_t._fields_ = [('__val', c_int * 2)]

# file /usr/include/bits/types.h, line 155, column 26
__fsid_t = __fsid_t

# file /usr/include/bits/types.h, line 156, column 27
__clock_t = c_long

# file /usr/include/bits/types.h, line 157, column 26
__rlim_t = c_ulong

# file /usr/include/bits/types.h, line 158, column 28
__rlim64_t = c_ulong

# file /usr/include/bits/types.h, line 159, column 24
__id_t = c_uint

# file /usr/include/bits/types.h, line 160, column 26
__time_t = c_long

# file /usr/include/bits/types.h, line 161, column 30
__useconds_t = c_uint

# file /usr/include/bits/types.h, line 162, column 31
__suseconds_t = c_long

# file /usr/include/bits/types.h, line 163, column 33
__suseconds64_t = c_long

# file /usr/include/bits/types.h, line 165, column 27
__daddr_t = c_int

# file /usr/include/bits/types.h, line 166, column 25
__key_t = c_int

# file /usr/include/bits/types.h, line 169, column 29
__clockid_t = c_int

# file /usr/include/bits/types.h, line 172, column 27
__timer_t = POINTER(None)

# file /usr/include/bits/types.h, line 175, column 29
__blksize_t = c_long

# file /usr/include/bits/types.h, line 180, column 28
__blkcnt_t = c_long

# file /usr/include/bits/types.h, line 181, column 30
__blkcnt64_t = c_long

# file /usr/include/bits/types.h, line 184, column 30
__fsblkcnt_t = c_ulong

# file /usr/include/bits/types.h, line 185, column 32
__fsblkcnt64_t = c_ulong

# file /usr/include/bits/types.h, line 188, column 30
__fsfilcnt_t = c_ulong

# file /usr/include/bits/types.h, line 189, column 32
__fsfilcnt64_t = c_ulong

# file /usr/include/bits/types.h, line 192, column 28
__fsword_t = c_long

# file /usr/include/bits/types.h, line 194, column 27
__ssize_t = c_long

# file /usr/include/bits/types.h, line 197, column 33
__syscall_slong_t = c_long

# file /usr/include/bits/types.h, line 199, column 33
__syscall_ulong_t = c_ulong

# file /usr/include/bits/types.h, line 203, column 19
__loff_t = c_long

# file /usr/include/bits/types.h, line 204, column 15
__caddr_t = c_char_p

# file /usr/include/bits/types.h, line 207, column 25
__intptr_t = c_long

# file /usr/include/bits/types.h, line 210, column 23
__socklen_t = c_uint

# file /usr/include/bits/types.h, line 215, column 13
__sig_atomic_t = c_int

# file /usr/include/sys/mman.h, line 29, column 17
off_t = c_long

# file /usr/include/sys/mman.h, line 37, column 18
mode_t = c_uint

# file /usr/include/sys/mman.h, line 57, column 14
DUMMYLIB_so.mmap.argtypes = [POINTER(None), c_int, c_int, c_int, c_int, c_long]
DUMMYLIB_so.mmap.restype = POINTER(None)

# file /usr/include/sys/mman.h, line 76, column 12
DUMMYLIB_so.munmap.argtypes = [POINTER(None), c_int]
DUMMYLIB_so.munmap.restype = c_int

# file /usr/include/sys/mman.h, line 81, column 12
DUMMYLIB_so.mprotect.argtypes = [POINTER(None), c_int, c_int]
DUMMYLIB_so.mprotect.restype = c_int

# file /usr/include/sys/mman.h, line 89, column 12
DUMMYLIB_so.msync.argtypes = [POINTER(None), c_int, c_int]
DUMMYLIB_so.msync.restype = c_int

# file /usr/include/sys/mman.h, line 94, column 12
DUMMYLIB_so.madvise.argtypes = [POINTER(None), c_int, c_int]
DUMMYLIB_so.madvise.restype = c_int

# file /usr/include/sys/mman.h, line 98, column 12
DUMMYLIB_so.posix_madvise.argtypes = [POINTER(None), c_int, c_int]
DUMMYLIB_so.posix_madvise.restype = c_int

# file /usr/include/sys/mman.h, line 103, column 12
DUMMYLIB_so.mlock.argtypes = [POINTER(None), c_int]
DUMMYLIB_so.mlock.restype = c_int

# file /usr/include/sys/mman.h, line 107, column 12
DUMMYLIB_so.munlock.argtypes = [POINTER(None), c_int]
DUMMYLIB_so.munlock.restype = c_int

# file /usr/include/sys/mman.h, line 113, column 12
DUMMYLIB_so.mlockall.argtypes = [c_int]
DUMMYLIB_so.mlockall.restype = c_int

# file /usr/include/sys/mman.h, line 117, column 12
DUMMYLIB_so.munlockall.argtypes = []
DUMMYLIB_so.munlockall.restype = c_int

# file /usr/include/sys/mman.h, line 125, column 12
DUMMYLIB_so.mincore.argtypes = [POINTER(None), c_int, POINTER(c_ubyte)]
DUMMYLIB_so.mincore.restype = c_int

# file /usr/include/sys/mman.h, line 146, column 12
DUMMYLIB_so.shm_open.argtypes = [c_char_p, c_int, c_uint]
DUMMYLIB_so.shm_open.restype = c_int

# file /usr/include/sys/mman.h, line 149, column 12
DUMMYLIB_so.shm_unlink.argtypes = [c_char_p]
DUMMYLIB_so.shm_unlink.restype = c_int

# file /usr/include/errno.h, line 37, column 13
DUMMYLIB_so.__errno_location.argtypes = []
DUMMYLIB_so.__errno_location.restype = POINTER(c_int)

# file /usr/include/string.h, line 43, column 14
DUMMYLIB_so.memcpy.argtypes = [POINTER(None), POINTER(None), c_int]
DUMMYLIB_so.memcpy.restype = POINTER(None)

# file /usr/include/string.h, line 47, column 14
DUMMYLIB_so.memmove.argtypes = [POINTER(None), POINTER(None), c_int]
DUMMYLIB_so.memmove.restype = POINTER(None)

# file /usr/include/string.h, line 54, column 14
DUMMYLIB_so.memccpy.argtypes = [POINTER(None), POINTER(None), c_int, c_int]
DUMMYLIB_so.memccpy.restype = POINTER(None)

# file /usr/include/string.h, line 61, column 14
DUMMYLIB_so.memset.argtypes = [POINTER(None), c_int, c_int]
DUMMYLIB_so.memset.restype = POINTER(None)

# file /usr/include/string.h, line 64, column 12
DUMMYLIB_so.memcmp.argtypes = [POINTER(None), POINTER(None), c_int]
DUMMYLIB_so.memcmp.restype = c_int

# file /usr/include/string.h, line 80, column 12
DUMMYLIB_so.__memcmpeq.argtypes = [POINTER(None), POINTER(None), c_int]
DUMMYLIB_so.__memcmpeq.restype = c_int

# file /usr/include/string.h, line 107, column 14
DUMMYLIB_so.memchr.argtypes = [POINTER(None), c_int, c_int]
DUMMYLIB_so.memchr.restype = POINTER(None)

# file /usr/include/string.h, line 141, column 14
DUMMYLIB_so.strcpy.argtypes = [c_char_p, c_char_p]
DUMMYLIB_so.strcpy.restype = c_char_p

# file /usr/include/string.h, line 144, column 14
DUMMYLIB_so.strncpy.argtypes = [c_char_p, c_char_p, c_int]
DUMMYLIB_so.strncpy.restype = c_char_p

# file /usr/include/string.h, line 149, column 14
DUMMYLIB_so.strcat.argtypes = [c_char_p, c_char_p]
DUMMYLIB_so.strcat.restype = c_char_p

# file /usr/include/string.h, line 152, column 14
DUMMYLIB_so.strncat.argtypes = [c_char_p, c_char_p, c_int]
DUMMYLIB_so.strncat.restype = c_char_p

# file /usr/include/string.h, line 156, column 12
DUMMYLIB_so.strcmp.argtypes = [c_char_p, c_char_p]
DUMMYLIB_so.strcmp.restype = c_int

# file /usr/include/string.h, line 159, column 12
DUMMYLIB_so.strncmp.argtypes = [c_char_p, c_char_p, c_int]
DUMMYLIB_so.strncmp.restype = c_int

# file /usr/include/string.h, line 163, column 12
DUMMYLIB_so.strcoll.argtypes = [c_char_p, c_char_p]
DUMMYLIB_so.strcoll.restype = c_int

# file /usr/include/string.h, line 166, column 15
DUMMYLIB_so.strxfrm.argtypes = [c_char_p, c_char_p, c_int]
DUMMYLIB_so.strxfrm.restype = c_int

# file /usr/include/bits/types/__locale_t.h, line 27, column 8

class __locale_struct(Structure):
    pass
__locale_struct._align_ = 8
__locale_struct._fields_ = [('__locales', POINTER(__locale_data) * 13), ('__ctype_b', POINTER(c_ushort)), ('__ctype_tolower', POINTER(c_int)), ('__ctype_toupper', POINTER(c_int)), ('__names', c_char_p * 13)]

# file /usr/include/bits/types/__locale_t.h, line 41, column 33
__locale_t = POINTER(__locale_struct)

# file /usr/include/bits/types/locale_t.h, line 24, column 20
locale_t = POINTER(__locale_struct)

# file /usr/include/string.h, line 175, column 12
DUMMYLIB_so.strcoll_l.argtypes = [c_char_p, c_char_p, POINTER(__locale_struct)]
DUMMYLIB_so.strcoll_l.restype = c_int

# file /usr/include/string.h, line 179, column 15
DUMMYLIB_so.strxfrm_l.argtypes = [c_char_p, c_char_p, c_int, POINTER(__locale_struct)]
DUMMYLIB_so.strxfrm_l.restype = c_int

# file /usr/include/string.h, line 187, column 14
DUMMYLIB_so.strdup.argtypes = [c_char_p]
DUMMYLIB_so.strdup.restype = c_char_p

# file /usr/include/string.h, line 195, column 14
DUMMYLIB_so.strndup.argtypes = [c_char_p, c_int]
DUMMYLIB_so.strndup.restype = c_char_p

# file /usr/include/string.h, line 246, column 14
DUMMYLIB_so.strchr.argtypes = [c_char_p, c_int]
DUMMYLIB_so.strchr.restype = c_char_p

# file /usr/include/string.h, line 273, column 14
DUMMYLIB_so.strrchr.argtypes = [c_char_p, c_int]
DUMMYLIB_so.strrchr.restype = c_char_p

# file /usr/include/string.h, line 286, column 14
DUMMYLIB_so.strchrnul.argtypes = [c_char_p, c_int]
DUMMYLIB_so.strchrnul.restype = c_char_p

# file /usr/include/string.h, line 293, column 15
DUMMYLIB_so.strcspn.argtypes = [c_char_p, c_char_p]
DUMMYLIB_so.strcspn.restype = c_int

# file /usr/include/string.h, line 297, column 15
DUMMYLIB_so.strspn.argtypes = [c_char_p, c_char_p]
DUMMYLIB_so.strspn.restype = c_int

# file /usr/include/string.h, line 323, column 14
DUMMYLIB_so.strpbrk.argtypes = [c_char_p, c_char_p]
DUMMYLIB_so.strpbrk.restype = c_char_p

# file /usr/include/string.h, line 350, column 14
DUMMYLIB_so.strstr.argtypes = [c_char_p, c_char_p]
DUMMYLIB_so.strstr.restype = c_char_p

# file /usr/include/string.h, line 356, column 14
DUMMYLIB_so.strtok.argtypes = [c_char_p, c_char_p]
DUMMYLIB_so.strtok.restype = c_char_p

# file /usr/include/string.h, line 361, column 14
DUMMYLIB_so.__strtok_r.argtypes = [c_char_p, c_char_p, POINTER(c_char_p)]
DUMMYLIB_so.__strtok_r.restype = c_char_p

# file /usr/include/string.h, line 366, column 14
DUMMYLIB_so.strtok_r.argtypes = [c_char_p, c_char_p, POINTER(c_char_p)]
DUMMYLIB_so.strtok_r.restype = c_char_p

# file /usr/include/string.h, line 380, column 14
DUMMYLIB_so.strcasestr.argtypes = [c_char_p, c_char_p]
DUMMYLIB_so.strcasestr.restype = c_char_p

# file /usr/include/string.h, line 389, column 14
DUMMYLIB_so.memmem.argtypes = [POINTER(None), c_int, POINTER(None), c_int]
DUMMYLIB_so.memmem.restype = POINTER(None)

# file /usr/include/string.h, line 397, column 14
DUMMYLIB_so.__mempcpy.argtypes = [POINTER(None), POINTER(None), c_int]
DUMMYLIB_so.__mempcpy.restype = POINTER(None)

# file /usr/include/string.h, line 400, column 14
DUMMYLIB_so.mempcpy.argtypes = [POINTER(None), POINTER(None), c_int]
DUMMYLIB_so.mempcpy.restype = POINTER(None)

# file /usr/include/string.h, line 407, column 15
DUMMYLIB_so.strlen.argtypes = [c_char_p]
DUMMYLIB_so.strlen.restype = c_int

# file /usr/include/string.h, line 413, column 15
DUMMYLIB_so.strnlen.argtypes = [c_char_p, c_int]
DUMMYLIB_so.strnlen.restype = c_int

# file /usr/include/string.h, line 419, column 14
DUMMYLIB_so.strerror.argtypes = [c_int]
DUMMYLIB_so.strerror.restype = c_char_p

# file /usr/include/string.h, line 432, column 12
DUMMYLIB_so.strerror_r.argtypes = [c_int, c_char_p, c_int]
DUMMYLIB_so.strerror_r.restype = c_int

# file /usr/include/string.h, line 458, column 14
DUMMYLIB_so.strerror_l.argtypes = [c_int, POINTER(__locale_struct)]
DUMMYLIB_so.strerror_l.restype = c_char_p

# file /usr/include/strings.h, line 34, column 12
DUMMYLIB_so.bcmp.argtypes = [POINTER(None), POINTER(None), c_int]
DUMMYLIB_so.bcmp.restype = c_int

# file /usr/include/strings.h, line 38, column 13
DUMMYLIB_so.bcopy.argtypes = [POINTER(None), POINTER(None), c_int]
DUMMYLIB_so.bcopy.restype = None

# file /usr/include/strings.h, line 42, column 13
DUMMYLIB_so.bzero.argtypes = [POINTER(None), c_int]
DUMMYLIB_so.bzero.restype = None

# file /usr/include/strings.h, line 68, column 14
DUMMYLIB_so.index.argtypes = [c_char_p, c_int]
DUMMYLIB_so.index.restype = c_char_p

# file /usr/include/strings.h, line 96, column 14
DUMMYLIB_so.rindex.argtypes = [c_char_p, c_int]
DUMMYLIB_so.rindex.restype = c_char_p

# file /usr/include/strings.h, line 104, column 12
DUMMYLIB_so.ffs.argtypes = [c_int]
DUMMYLIB_so.ffs.restype = c_int

# file /usr/include/strings.h, line 110, column 12
DUMMYLIB_so.ffsl.argtypes = [c_long]
DUMMYLIB_so.ffsl.restype = c_int

# file /usr/include/strings.h, line 111, column 26
DUMMYLIB_so.ffsll.argtypes = [c_long]
DUMMYLIB_so.ffsll.restype = c_int

# file /usr/include/strings.h, line 116, column 12
DUMMYLIB_so.strcasecmp.argtypes = [c_char_p, c_char_p]
DUMMYLIB_so.strcasecmp.restype = c_int

# file /usr/include/strings.h, line 120, column 12
DUMMYLIB_so.strncasecmp.argtypes = [c_char_p, c_char_p, c_int]
DUMMYLIB_so.strncasecmp.restype = c_int

# file /usr/include/strings.h, line 128, column 12
DUMMYLIB_so.strcasecmp_l.argtypes = [c_char_p, c_char_p, POINTER(__locale_struct)]
DUMMYLIB_so.strcasecmp_l.restype = c_int

# file /usr/include/strings.h, line 133, column 12
DUMMYLIB_so.strncasecmp_l.argtypes = [c_char_p, c_char_p, c_int, POINTER(__locale_struct)]
DUMMYLIB_so.strncasecmp_l.restype = c_int

# file /usr/include/string.h, line 466, column 13
DUMMYLIB_so.explicit_bzero.argtypes = [POINTER(None), c_int]
DUMMYLIB_so.explicit_bzero.restype = None

# file /usr/include/string.h, line 471, column 14
DUMMYLIB_so.strsep.argtypes = [POINTER(c_char_p), c_char_p]
DUMMYLIB_so.strsep.restype = c_char_p

# file /usr/include/string.h, line 478, column 14
DUMMYLIB_so.strsignal.argtypes = [c_int]
DUMMYLIB_so.strsignal.restype = c_char_p

# file /usr/include/string.h, line 489, column 14
DUMMYLIB_so.__stpcpy.argtypes = [c_char_p, c_char_p]
DUMMYLIB_so.__stpcpy.restype = c_char_p

# file /usr/include/string.h, line 491, column 14
DUMMYLIB_so.stpcpy.argtypes = [c_char_p, c_char_p]
DUMMYLIB_so.stpcpy.restype = c_char_p

# file /usr/include/string.h, line 496, column 14
DUMMYLIB_so.__stpncpy.argtypes = [c_char_p, c_char_p, c_int]
DUMMYLIB_so.__stpncpy.restype = c_char_p

# file /usr/include/string.h, line 499, column 14
DUMMYLIB_so.stpncpy.argtypes = [c_char_p, c_char_p, c_int]
DUMMYLIB_so.stpncpy.restype = c_char_p

# file /usr/include/string.h, line 506, column 15
DUMMYLIB_so.strlcpy.argtypes = [c_char_p, c_char_p, c_int]
DUMMYLIB_so.strlcpy.restype = c_int

# file /usr/include/string.h, line 512, column 15
DUMMYLIB_so.strlcat.argtypes = [c_char_p, c_char_p, c_int]
DUMMYLIB_so.strlcat.restype = c_int

# file /usr/include/bits/floatn.h, line 83, column 24
__cfloat128 = c_complex

# file /usr/include/bits/floatn.h, line 97, column 20
_Float128 = c_float128

# file /usr/include/bits/floatn-common.h, line 214, column 15
_Float32 = c_float

# file /usr/include/bits/floatn-common.h, line 251, column 16
_Float64 = c_double

# file /usr/include/bits/floatn-common.h, line 268, column 16
_Float32x = c_double

# file /usr/include/bits/floatn-common.h, line 285, column 21
_Float64x = c_longdouble

# file /usr/include/stdlib.h, line 59, column 9

class div_t(Structure):
    pass
div_t._align_ = 4
div_t._fields_ = [('quot', c_int), ('rem', c_int)]

# file /usr/include/stdlib.h, line 63, column 5
div_t = div_t

# file /usr/include/stdlib.h, line 67, column 9

class ldiv_t(Structure):
    pass
ldiv_t._align_ = 8
ldiv_t._fields_ = [('quot', c_long), ('rem', c_long)]

# file /usr/include/stdlib.h, line 71, column 5
ldiv_t = ldiv_t

# file /usr/include/stdlib.h, line 77, column 23

class lldiv_t(Structure):
    pass
lldiv_t._align_ = 8
lldiv_t._fields_ = [('quot', c_long), ('rem', c_long)]

# file /usr/include/stdlib.h, line 81, column 5
lldiv_t = lldiv_t

# file /usr/include/stdlib.h, line 98, column 15
DUMMYLIB_so.__ctype_get_mb_cur_max.argtypes = []
DUMMYLIB_so.__ctype_get_mb_cur_max.restype = c_int

# file /usr/include/stdlib.h, line 102, column 15
DUMMYLIB_so.atof.argtypes = [c_char_p]
DUMMYLIB_so.atof.restype = c_double

# file /usr/include/stdlib.h, line 105, column 12
DUMMYLIB_so.atoi.argtypes = [c_char_p]
DUMMYLIB_so.atoi.restype = c_int

# file /usr/include/stdlib.h, line 108, column 17
DUMMYLIB_so.atol.argtypes = [c_char_p]
DUMMYLIB_so.atol.restype = c_long

# file /usr/include/stdlib.h, line 113, column 36
DUMMYLIB_so.atoll.argtypes = [c_char_p]
DUMMYLIB_so.atoll.restype = c_long

# file /usr/include/stdlib.h, line 118, column 15
DUMMYLIB_so.strtod.argtypes = [c_char_p, POINTER(c_char_p)]
DUMMYLIB_so.strtod.restype = c_double

# file /usr/include/stdlib.h, line 124, column 14
DUMMYLIB_so.strtof.argtypes = [c_char_p, POINTER(c_char_p)]
DUMMYLIB_so.strtof.restype = c_float

# file /usr/include/stdlib.h, line 127, column 20
DUMMYLIB_so.strtold.argtypes = [c_char_p, POINTER(c_char_p)]
DUMMYLIB_so.strtold.restype = c_longdouble

# file /usr/include/stdlib.h, line 177, column 17
DUMMYLIB_so.strtol.argtypes = [c_char_p, POINTER(c_char_p), c_int]
DUMMYLIB_so.strtol.restype = c_long

# file /usr/include/stdlib.h, line 181, column 26
DUMMYLIB_so.strtoul.argtypes = [c_char_p, POINTER(c_char_p), c_int]
DUMMYLIB_so.strtoul.restype = c_ulong

# file /usr/include/stdlib.h, line 188, column 22
DUMMYLIB_so.strtoq.argtypes = [c_char_p, POINTER(c_char_p), c_int]
DUMMYLIB_so.strtoq.restype = c_long

# file /usr/include/stdlib.h, line 193, column 31
DUMMYLIB_so.strtouq.argtypes = [c_char_p, POINTER(c_char_p), c_int]
DUMMYLIB_so.strtouq.restype = c_ulong

# file /usr/include/stdlib.h, line 201, column 22
DUMMYLIB_so.strtoll.argtypes = [c_char_p, POINTER(c_char_p), c_int]
DUMMYLIB_so.strtoll.restype = c_long

# file /usr/include/stdlib.h, line 206, column 31
DUMMYLIB_so.strtoull.argtypes = [c_char_p, POINTER(c_char_p), c_int]
DUMMYLIB_so.strtoull.restype = c_ulong

# file /usr/include/stdlib.h, line 505, column 14
DUMMYLIB_so.l64a.argtypes = [c_long]
DUMMYLIB_so.l64a.restype = c_char_p

# file /usr/include/stdlib.h, line 508, column 17
DUMMYLIB_so.a64l.argtypes = [c_char_p]
DUMMYLIB_so.a64l.restype = c_long

# file /usr/include/sys/types.h, line 33, column 18
u_char = c_ubyte

# file /usr/include/sys/types.h, line 34, column 19
u_short = c_ushort

# file /usr/include/sys/types.h, line 35, column 17
u_int = c_uint

# file /usr/include/sys/types.h, line 36, column 18
u_long = c_ulong

# file /usr/include/sys/types.h, line 37, column 18
quad_t = c_long

# file /usr/include/sys/types.h, line 38, column 20
u_quad_t = c_ulong

# file /usr/include/sys/types.h, line 39, column 18
fsid_t = __fsid_t

# file /usr/include/sys/types.h, line 42, column 18
loff_t = c_long

# file /usr/include/sys/types.h, line 47, column 17
ino_t = c_ulong

# file /usr/include/sys/types.h, line 59, column 17
dev_t = c_ulong

# file /usr/include/sys/types.h, line 64, column 17
gid_t = c_uint

# file /usr/include/sys/types.h, line 74, column 19
nlink_t = c_ulong

# file /usr/include/sys/types.h, line 79, column 17
uid_t = c_uint

# file /usr/include/sys/types.h, line 97, column 17
pid_t = c_int

# file /usr/include/sys/types.h, line 103, column 16
id_t = c_uint

# file /usr/include/sys/types.h, line 108, column 19
ssize_t = c_long

# file /usr/include/sys/types.h, line 114, column 19
daddr_t = c_int

# file /usr/include/sys/types.h, line 115, column 19
caddr_t = c_char_p

# file /usr/include/sys/types.h, line 121, column 17
key_t = c_int

# file /usr/include/bits/types/clock_t.h, line 7, column 19
clock_t = c_long

# file /usr/include/bits/types/clockid_t.h, line 7, column 21
clockid_t = c_int

# file /usr/include/bits/types/time_t.h, line 10, column 18
time_t = c_long

# file /usr/include/bits/types/timer_t.h, line 7, column 19
timer_t = POINTER(None)

# file /usr/include/sys/types.h, line 148, column 27
ulong = c_ulong

# file /usr/include/sys/types.h, line 149, column 28
ushort = c_ushort

# file /usr/include/sys/types.h, line 150, column 22
uint = c_uint

# file /usr/include/bits/stdint-intn.h, line 24, column 18
int8_t = c_byte

# file /usr/include/bits/stdint-intn.h, line 25, column 19
int16_t = c_short

# file /usr/include/bits/stdint-intn.h, line 26, column 19
int32_t = c_int

# file /usr/include/bits/stdint-intn.h, line 27, column 19
int64_t = c_long

# file /usr/include/sys/types.h, line 158, column 19
u_int8_t = c_ubyte

# file /usr/include/sys/types.h, line 159, column 20
u_int16_t = c_ushort

# file /usr/include/sys/types.h, line 160, column 20
u_int32_t = c_uint

# file /usr/include/sys/types.h, line 161, column 20
u_int64_t = c_ulong

# file /usr/include/sys/types.h, line 164, column 13
register_t = c_long

# file /usr/include/bits/byteswap.h, line 34, column 1
DUMMYLIB_so.__bswap_16.argtypes = [c_ushort]
DUMMYLIB_so.__bswap_16.restype = c_ushort

# file /usr/include/bits/byteswap.h, line 49, column 1
DUMMYLIB_so.__bswap_32.argtypes = [c_uint]
DUMMYLIB_so.__bswap_32.restype = c_uint

# file /usr/include/bits/byteswap.h, line 70, column 1
DUMMYLIB_so.__bswap_64.argtypes = [c_ulong]
DUMMYLIB_so.__bswap_64.restype = c_ulong

# file /usr/include/bits/uintn-identity.h, line 33, column 1
DUMMYLIB_so.__uint16_identity.argtypes = [c_ushort]
DUMMYLIB_so.__uint16_identity.restype = c_ushort

# file /usr/include/bits/uintn-identity.h, line 39, column 1
DUMMYLIB_so.__uint32_identity.argtypes = [c_uint]
DUMMYLIB_so.__uint32_identity.restype = c_uint

# file /usr/include/bits/uintn-identity.h, line 45, column 1
DUMMYLIB_so.__uint64_identity.argtypes = [c_ulong]
DUMMYLIB_so.__uint64_identity.restype = c_ulong

# file /usr/include/bits/types/__sigset_t.h, line 5, column 9

class __sigset_t(Structure):
    pass
__sigset_t._align_ = 8
__sigset_t._fields_ = [('__val', c_ulong * 16)]

# file /usr/include/bits/types/__sigset_t.h, line 8, column 3
__sigset_t = __sigset_t

# file /usr/include/bits/types/sigset_t.h, line 7, column 20
sigset_t = __sigset_t

# file /usr/include/bits/types/struct_timeval.h, line 8, column 8

class timeval(Structure):
    pass
timeval._align_ = 8
timeval._fields_ = [('tv_sec', c_long), ('tv_usec', c_long)]

# file /usr/include/bits/types/struct_timespec.h, line 11, column 8

class timespec(Structure):
    pass
timespec._align_ = 8
timespec._fields_ = [('tv_sec', c_long), ('tv_nsec', c_long)]

# file /usr/include/sys/select.h, line 43, column 23
suseconds_t = c_long

# file /usr/include/sys/select.h, line 49, column 18
__fd_mask = c_long

# file /usr/include/sys/select.h, line 59, column 9

class fd_set(Structure):
    pass
fd_set._align_ = 8
fd_set._fields_ = [('__fds_bits', c_long * 16)]

# file /usr/include/sys/select.h, line 70, column 5
fd_set = fd_set

# file /usr/include/sys/select.h, line 77, column 19
fd_mask = c_long

# file /usr/include/sys/select.h, line 102, column 12
DUMMYLIB_so.select.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timeval)]
DUMMYLIB_so.select.restype = c_int

# file /usr/include/sys/select.h, line 127, column 12
DUMMYLIB_so.pselect.argtypes = [c_int, POINTER(fd_set), POINTER(fd_set), POINTER(fd_set), POINTER(timespec), POINTER(__sigset_t)]
DUMMYLIB_so.pselect.restype = c_int

# file /usr/include/sys/types.h, line 185, column 21
blksize_t = c_long

# file /usr/include/sys/types.h, line 192, column 20
blkcnt_t = c_long

# file /usr/include/sys/types.h, line 196, column 22
fsblkcnt_t = c_ulong

# file /usr/include/sys/types.h, line 200, column 22
fsfilcnt_t = c_ulong

# file /usr/include/bits/atomic_wide_counter.h, line 25, column 9

class __atomic_wide_counter(Union):

    class _usr_include_bits_atomic_wide_counter_h_28_3_(Structure):
        pass
    _usr_include_bits_atomic_wide_counter_h_28_3_._fields_ = [('__low', c_uint), ('__high', c_uint)]
__atomic_wide_counter._align_ = 8
__atomic_wide_counter._fields_ = [('__value64', c_ulong), ('__value32', _usr_include_bits_atomic_wide_counter_h_28_3_)]

# file /usr/include/bits/atomic_wide_counter.h, line 33, column 3
__atomic_wide_counter = __atomic_wide_counter

# file /usr/include/bits/thread-shared-types.h, line 51, column 16

class __pthread_internal_list(Structure):
    pass
__pthread_internal_list._align_ = 8
__pthread_internal_list._fields_ = [('__prev', POINTER(__pthread_internal_list)), ('__next', POINTER(__pthread_internal_list))]

# file /usr/include/bits/thread-shared-types.h, line 55, column 3
__pthread_list_t = __pthread_internal_list

# file /usr/include/bits/thread-shared-types.h, line 57, column 16

class __pthread_internal_slist(Structure):
    pass
__pthread_internal_slist._align_ = 8
__pthread_internal_slist._fields_ = [('__next', POINTER(__pthread_internal_slist))]

# file /usr/include/bits/thread-shared-types.h, line 60, column 3
__pthread_slist_t = __pthread_internal_slist

# file /usr/include/bits/struct_mutex.h, line 22, column 8

class __pthread_mutex_s(Structure):

    class __pthread_internal_list(Structure):
        pass
    __pthread_internal_list._fields_ = [('__prev', POINTER(__pthread_internal_list)), ('__next', POINTER(__pthread_internal_list))]
__pthread_mutex_s._align_ = 8
__pthread_mutex_s._fields_ = [('__lock', c_int), ('__count', c_uint), ('__owner', c_int), ('__nusers', c_uint), ('__kind', c_int), ('__spins', c_short), ('__elision', c_short), ('__list', __pthread_internal_list)]

# file /usr/include/bits/struct_rwlock.h, line 23, column 8

class __pthread_rwlock_arch_t(Structure):
    pass
__pthread_rwlock_arch_t._align_ = 8
__pthread_rwlock_arch_t._fields_ = [('__readers', c_uint), ('__writers', c_uint), ('__wrphase_futex', c_uint), ('__writers_futex', c_uint), ('__pad3', c_uint), ('__pad4', c_uint), ('__cur_writer', c_int), ('__shared', c_int), ('__rwelision', c_byte), ('__pad1', c_ubyte * 7), ('__pad2', c_ulong), ('__flags', c_uint)]

# file /usr/include/bits/thread-shared-types.h, line 94, column 8

class __pthread_cond_s(Structure):

    class __atomic_wide_counter(Union):

        class _usr_include_bits_atomic_wide_counter_h_28_3_(Structure):
            pass
        _usr_include_bits_atomic_wide_counter_h_28_3_._fields_ = [('__low', c_uint), ('__high', c_uint)]
    __atomic_wide_counter._fields_ = [('__value64', c_ulong), ('__value32', _usr_include_bits_atomic_wide_counter_h_28_3_)]

    class __atomic_wide_counter(Union):

        class _usr_include_bits_atomic_wide_counter_h_28_3_(Structure):
            pass
        _usr_include_bits_atomic_wide_counter_h_28_3_._fields_ = [('__low', c_uint), ('__high', c_uint)]
    __atomic_wide_counter._fields_ = [('__value64', c_ulong), ('__value32', _usr_include_bits_atomic_wide_counter_h_28_3_)]
__pthread_cond_s._align_ = 8
__pthread_cond_s._fields_ = [('__wseq', __atomic_wide_counter), ('__g1_start', __atomic_wide_counter), ('__g_size', c_uint * 2), ('__g1_orig_size', c_uint), ('__wrefs', c_uint), ('__g_signals', c_uint * 2), ('__unused_initialized_1', c_uint), ('__unused_initialized_2', c_uint)]

# file /usr/include/bits/thread-shared-types.h, line 106, column 22
__tss_t = c_uint

# file /usr/include/bits/thread-shared-types.h, line 107, column 27
__thrd_t = c_ulong

# file /usr/include/bits/thread-shared-types.h, line 109, column 9

class __once_flag(Structure):
    pass
__once_flag._align_ = 4
__once_flag._fields_ = [('__data', c_int)]

# file /usr/include/bits/thread-shared-types.h, line 112, column 3
__once_flag = __once_flag

# file /usr/include/bits/pthreadtypes.h, line 27, column 27
pthread_t = c_ulong

# file /usr/include/bits/pthreadtypes.h, line 32, column 9

class pthread_mutexattr_t(Union):
    pass
pthread_mutexattr_t._align_ = 4
pthread_mutexattr_t._fields_ = [('__size', c_char * 4), ('__align', c_int)]

# file /usr/include/bits/pthreadtypes.h, line 36, column 3
pthread_mutexattr_t = pthread_mutexattr_t

# file /usr/include/bits/pthreadtypes.h, line 41, column 9

class pthread_condattr_t(Union):
    pass
pthread_condattr_t._align_ = 4
pthread_condattr_t._fields_ = [('__size', c_char * 4), ('__align', c_int)]

# file /usr/include/bits/pthreadtypes.h, line 45, column 3
pthread_condattr_t = pthread_condattr_t

# file /usr/include/bits/pthreadtypes.h, line 49, column 22
pthread_key_t = c_uint

# file /usr/include/bits/pthreadtypes.h, line 53, column 30
pthread_once_t = c_int

# file /usr/include/bits/pthreadtypes.h, line 56, column 7

class pthread_attr_t(Union):
    pass
pthread_attr_t._align_ = 8
pthread_attr_t._fields_ = [('__size', c_char * 56), ('__align', c_long)]

# file /usr/include/bits/pthreadtypes.h, line 62, column 30
pthread_attr_t = pthread_attr_t

# file /usr/include/bits/pthreadtypes.h, line 67, column 9

class pthread_mutex_t(Union):

    class __pthread_mutex_s(Structure):

        class __pthread_internal_list(Structure):
            pass
        __pthread_internal_list._fields_ = [('__prev', POINTER(__pthread_internal_list)), ('__next', POINTER(__pthread_internal_list))]
    __pthread_mutex_s._fields_ = [('__lock', c_int), ('__count', c_uint), ('__owner', c_int), ('__nusers', c_uint), ('__kind', c_int), ('__spins', c_short), ('__elision', c_short), ('__list', __pthread_internal_list)]
pthread_mutex_t._align_ = 8
pthread_mutex_t._fields_ = [('__data', __pthread_mutex_s), ('__size', c_char * 40), ('__align', c_long)]

# file /usr/include/bits/pthreadtypes.h, line 72, column 3
pthread_mutex_t = pthread_mutex_t

# file /usr/include/bits/pthreadtypes.h, line 75, column 9

class pthread_cond_t(Union):

    class __pthread_cond_s(Structure):

        class __atomic_wide_counter(Union):

            class _usr_include_bits_atomic_wide_counter_h_28_3_(Structure):
                pass
            _usr_include_bits_atomic_wide_counter_h_28_3_._fields_ = [('__low', c_uint), ('__high', c_uint)]
        __atomic_wide_counter._fields_ = [('__value64', c_ulong), ('__value32', _usr_include_bits_atomic_wide_counter_h_28_3_)]

        class __atomic_wide_counter(Union):

            class _usr_include_bits_atomic_wide_counter_h_28_3_(Structure):
                pass
            _usr_include_bits_atomic_wide_counter_h_28_3_._fields_ = [('__low', c_uint), ('__high', c_uint)]
        __atomic_wide_counter._fields_ = [('__value64', c_ulong), ('__value32', _usr_include_bits_atomic_wide_counter_h_28_3_)]
    __pthread_cond_s._fields_ = [('__wseq', __atomic_wide_counter), ('__g1_start', __atomic_wide_counter), ('__g_size', c_uint * 2), ('__g1_orig_size', c_uint), ('__wrefs', c_uint), ('__g_signals', c_uint * 2), ('__unused_initialized_1', c_uint), ('__unused_initialized_2', c_uint)]
pthread_cond_t._align_ = 8
pthread_cond_t._fields_ = [('__data', __pthread_cond_s), ('__size', c_char * 48), ('__align', c_long)]

# file /usr/include/bits/pthreadtypes.h, line 80, column 3
pthread_cond_t = pthread_cond_t

# file /usr/include/bits/pthreadtypes.h, line 86, column 9

class pthread_rwlock_t(Union):

    class __pthread_rwlock_arch_t(Structure):
        pass
    __pthread_rwlock_arch_t._fields_ = [('__readers', c_uint), ('__writers', c_uint), ('__wrphase_futex', c_uint), ('__writers_futex', c_uint), ('__pad3', c_uint), ('__pad4', c_uint), ('__cur_writer', c_int), ('__shared', c_int), ('__rwelision', c_byte), ('__pad1', c_ubyte * 7), ('__pad2', c_ulong), ('__flags', c_uint)]
pthread_rwlock_t._align_ = 8
pthread_rwlock_t._fields_ = [('__data', __pthread_rwlock_arch_t), ('__size', c_char * 56), ('__align', c_long)]

# file /usr/include/bits/pthreadtypes.h, line 91, column 3
pthread_rwlock_t = pthread_rwlock_t

# file /usr/include/bits/pthreadtypes.h, line 93, column 9

class pthread_rwlockattr_t(Union):
    pass
pthread_rwlockattr_t._align_ = 8
pthread_rwlockattr_t._fields_ = [('__size', c_char * 8), ('__align', c_long)]

# file /usr/include/bits/pthreadtypes.h, line 97, column 3
pthread_rwlockattr_t = pthread_rwlockattr_t

# file /usr/include/bits/pthreadtypes.h, line 103, column 22
pthread_spinlock_t = c_int

# file /usr/include/bits/pthreadtypes.h, line 108, column 9

class pthread_barrier_t(Union):
    pass
pthread_barrier_t._align_ = 8
pthread_barrier_t._fields_ = [('__size', c_char * 32), ('__align', c_long)]

# file /usr/include/bits/pthreadtypes.h, line 112, column 3
pthread_barrier_t = pthread_barrier_t

# file /usr/include/bits/pthreadtypes.h, line 114, column 9

class pthread_barrierattr_t(Union):
    pass
pthread_barrierattr_t._align_ = 4
pthread_barrierattr_t._fields_ = [('__size', c_char * 4), ('__align', c_int)]

# file /usr/include/bits/pthreadtypes.h, line 118, column 3
pthread_barrierattr_t = pthread_barrierattr_t

# file /usr/include/stdlib.h, line 521, column 17
DUMMYLIB_so.random.argtypes = []
DUMMYLIB_so.random.restype = c_long

# file /usr/include/stdlib.h, line 524, column 13
DUMMYLIB_so.srandom.argtypes = [c_uint]
DUMMYLIB_so.srandom.restype = None

# file /usr/include/stdlib.h, line 530, column 14
DUMMYLIB_so.initstate.argtypes = [c_uint, c_char_p, c_int]
DUMMYLIB_so.initstate.restype = c_char_p

# file /usr/include/stdlib.h, line 535, column 14
DUMMYLIB_so.setstate.argtypes = [c_char_p]
DUMMYLIB_so.setstate.restype = c_char_p

# file /usr/include/stdlib.h, line 543, column 8

class random_data(Structure):
    pass
random_data._align_ = 8
random_data._fields_ = [('fptr', POINTER(c_int)), ('rptr', POINTER(c_int)), ('state', POINTER(c_int)), ('rand_type', c_int), ('rand_deg', c_int), ('rand_sep', c_int), ('end_ptr', POINTER(c_int))]

# file /usr/include/stdlib.h, line 554, column 12
DUMMYLIB_so.random_r.argtypes = [POINTER(random_data), POINTER(c_int)]
DUMMYLIB_so.random_r.restype = c_int

# file /usr/include/stdlib.h, line 557, column 12
DUMMYLIB_so.srandom_r.argtypes = [c_uint, POINTER(random_data)]
DUMMYLIB_so.srandom_r.restype = c_int

# file /usr/include/stdlib.h, line 560, column 12
DUMMYLIB_so.initstate_r.argtypes = [c_uint, c_char_p, c_int, POINTER(random_data)]
DUMMYLIB_so.initstate_r.restype = c_int

# file /usr/include/stdlib.h, line 565, column 12
DUMMYLIB_so.setstate_r.argtypes = [c_char_p, POINTER(random_data)]
DUMMYLIB_so.setstate_r.restype = c_int

# file /usr/include/stdlib.h, line 573, column 12
DUMMYLIB_so.rand.argtypes = []
DUMMYLIB_so.rand.restype = c_int

# file /usr/include/stdlib.h, line 575, column 13
DUMMYLIB_so.srand.argtypes = [c_uint]
DUMMYLIB_so.srand.restype = None

# file /usr/include/stdlib.h, line 579, column 12
DUMMYLIB_so.rand_r.argtypes = [POINTER(c_uint)]
DUMMYLIB_so.rand_r.restype = c_int

# file /usr/include/stdlib.h, line 587, column 15
DUMMYLIB_so.drand48.argtypes = []
DUMMYLIB_so.drand48.restype = c_double

# file /usr/include/stdlib.h, line 588, column 15
DUMMYLIB_so.erand48.argtypes = [c_ushort * 3]
DUMMYLIB_so.erand48.restype = c_double

# file /usr/include/stdlib.h, line 591, column 17
DUMMYLIB_so.lrand48.argtypes = []
DUMMYLIB_so.lrand48.restype = c_long

# file /usr/include/stdlib.h, line 592, column 17
DUMMYLIB_so.nrand48.argtypes = [c_ushort * 3]
DUMMYLIB_so.nrand48.restype = c_long

# file /usr/include/stdlib.h, line 596, column 17
DUMMYLIB_so.mrand48.argtypes = []
DUMMYLIB_so.mrand48.restype = c_long

# file /usr/include/stdlib.h, line 597, column 17
DUMMYLIB_so.jrand48.argtypes = [c_ushort * 3]
DUMMYLIB_so.jrand48.restype = c_long

# file /usr/include/stdlib.h, line 601, column 13
DUMMYLIB_so.srand48.argtypes = [c_long]
DUMMYLIB_so.srand48.restype = None

# file /usr/include/stdlib.h, line 602, column 28
DUMMYLIB_so.seed48.argtypes = [c_ushort * 3]
DUMMYLIB_so.seed48.restype = POINTER(c_ushort)

# file /usr/include/stdlib.h, line 604, column 13
DUMMYLIB_so.lcong48.argtypes = [c_ushort * 7]
DUMMYLIB_so.lcong48.restype = None

# file /usr/include/stdlib.h, line 610, column 8

class drand48_data(Structure):
    pass
drand48_data._align_ = 8
drand48_data._fields_ = [('__x', c_ushort * 3), ('__old_x', c_ushort * 3), ('__c', c_ushort), ('__init', c_ushort), ('__a', c_ulong)]

# file /usr/include/stdlib.h, line 621, column 12
DUMMYLIB_so.drand48_r.argtypes = [POINTER(drand48_data), POINTER(c_double)]
DUMMYLIB_so.drand48_r.restype = c_int

# file /usr/include/stdlib.h, line 623, column 12
DUMMYLIB_so.erand48_r.argtypes = [c_ushort * 3, POINTER(drand48_data), POINTER(c_double)]
DUMMYLIB_so.erand48_r.restype = c_int

# file /usr/include/stdlib.h, line 628, column 12
DUMMYLIB_so.lrand48_r.argtypes = [POINTER(drand48_data), POINTER(c_long)]
DUMMYLIB_so.lrand48_r.restype = c_int

# file /usr/include/stdlib.h, line 631, column 12
DUMMYLIB_so.nrand48_r.argtypes = [c_ushort * 3, POINTER(drand48_data), POINTER(c_long)]
DUMMYLIB_so.nrand48_r.restype = c_int

# file /usr/include/stdlib.h, line 637, column 12
DUMMYLIB_so.mrand48_r.argtypes = [POINTER(drand48_data), POINTER(c_long)]
DUMMYLIB_so.mrand48_r.restype = c_int

# file /usr/include/stdlib.h, line 640, column 12
DUMMYLIB_so.jrand48_r.argtypes = [c_ushort * 3, POINTER(drand48_data), POINTER(c_long)]
DUMMYLIB_so.jrand48_r.restype = c_int

# file /usr/include/stdlib.h, line 646, column 12
DUMMYLIB_so.srand48_r.argtypes = [c_long, POINTER(drand48_data)]
DUMMYLIB_so.srand48_r.restype = c_int

# file /usr/include/stdlib.h, line 649, column 12
DUMMYLIB_so.seed48_r.argtypes = [c_ushort * 3, POINTER(drand48_data)]
DUMMYLIB_so.seed48_r.restype = c_int

# file /usr/include/stdlib.h, line 652, column 12
DUMMYLIB_so.lcong48_r.argtypes = [c_ushort * 7, POINTER(drand48_data)]
DUMMYLIB_so.lcong48_r.restype = c_int

# file /usr/include/stdlib.h, line 657, column 19
DUMMYLIB_so.arc4random.argtypes = []
DUMMYLIB_so.arc4random.restype = c_uint

# file /usr/include/stdlib.h, line 661, column 13
DUMMYLIB_so.arc4random_buf.argtypes = [POINTER(None), c_int]
DUMMYLIB_so.arc4random_buf.restype = None

# file /usr/include/stdlib.h, line 666, column 19
DUMMYLIB_so.arc4random_uniform.argtypes = [c_uint]
DUMMYLIB_so.arc4random_uniform.restype = c_uint

# file /usr/include/stdlib.h, line 672, column 14
DUMMYLIB_so.malloc.argtypes = [c_int]
DUMMYLIB_so.malloc.restype = POINTER(None)

# file /usr/include/stdlib.h, line 675, column 14
DUMMYLIB_so.calloc.argtypes = [c_int, c_int]
DUMMYLIB_so.calloc.restype = POINTER(None)

# file /usr/include/stdlib.h, line 683, column 14
DUMMYLIB_so.realloc.argtypes = [POINTER(None), c_int]
DUMMYLIB_so.realloc.restype = POINTER(None)

# file /usr/include/stdlib.h, line 687, column 13
DUMMYLIB_so.free.argtypes = [POINTER(None)]
DUMMYLIB_so.free.restype = None

# file /usr/include/stdlib.h, line 695, column 14
DUMMYLIB_so.reallocarray.argtypes = [POINTER(None), c_int, c_int]
DUMMYLIB_so.reallocarray.restype = POINTER(None)

# file /usr/include/stdlib.h, line 701, column 14
DUMMYLIB_so.reallocarray.argtypes = [POINTER(None), c_int, c_int]
DUMMYLIB_so.reallocarray.restype = POINTER(None)

# file /usr/include/alloca.h, line 32, column 14
DUMMYLIB_so.alloca.argtypes = [c_int]
DUMMYLIB_so.alloca.restype = POINTER(None)

# file /usr/include/stdlib.h, line 712, column 14
DUMMYLIB_so.valloc.argtypes = [c_int]
DUMMYLIB_so.valloc.restype = POINTER(None)

# file /usr/include/stdlib.h, line 718, column 12
DUMMYLIB_so.posix_memalign.argtypes = [POINTER(POINTER(None)), c_int, c_int]
DUMMYLIB_so.posix_memalign.restype = c_int

# file /usr/include/stdlib.h, line 724, column 14
DUMMYLIB_so.aligned_alloc.argtypes = [c_int, c_int]
DUMMYLIB_so.aligned_alloc.restype = POINTER(None)

# file /usr/include/stdlib.h, line 730, column 13
DUMMYLIB_so.abort.argtypes = []
DUMMYLIB_so.abort.restype = None

# file /usr/include/stdlib.h, line 734, column 12
DUMMYLIB_so.atexit.argtypes = [CFUNCTYPE(None)]
DUMMYLIB_so.atexit.restype = c_int

# file /usr/include/stdlib.h, line 742, column 12
DUMMYLIB_so.at_quick_exit.argtypes = [CFUNCTYPE(None)]
DUMMYLIB_so.at_quick_exit.restype = c_int

# file /usr/include/stdlib.h, line 749, column 12
DUMMYLIB_so.on_exit.argtypes = [CFUNCTYPE(None, c_int, POINTER(None)), POINTER(None)]
DUMMYLIB_so.on_exit.restype = c_int

# file /usr/include/stdlib.h, line 756, column 13
DUMMYLIB_so.exit.argtypes = [c_int]
DUMMYLIB_so.exit.restype = None

# file /usr/include/stdlib.h, line 762, column 13
DUMMYLIB_so.quick_exit.argtypes = [c_int]
DUMMYLIB_so.quick_exit.restype = None

# file /usr/include/stdlib.h, line 768, column 13
DUMMYLIB_so._Exit.argtypes = [c_int]
DUMMYLIB_so._Exit.restype = None

# file /usr/include/stdlib.h, line 773, column 14
DUMMYLIB_so.getenv.argtypes = [c_char_p]
DUMMYLIB_so.getenv.restype = c_char_p

# file /usr/include/stdlib.h, line 786, column 12
DUMMYLIB_so.putenv.argtypes = [c_char_p]
DUMMYLIB_so.putenv.restype = c_int

# file /usr/include/stdlib.h, line 792, column 12
DUMMYLIB_so.setenv.argtypes = [c_char_p, c_char_p, c_int]
DUMMYLIB_so.setenv.restype = c_int

# file /usr/include/stdlib.h, line 796, column 12
DUMMYLIB_so.unsetenv.argtypes = [c_char_p]
DUMMYLIB_so.unsetenv.restype = c_int

# file /usr/include/stdlib.h, line 803, column 12
DUMMYLIB_so.clearenv.argtypes = []
DUMMYLIB_so.clearenv.restype = c_int

# file /usr/include/stdlib.h, line 814, column 14
DUMMYLIB_so.mktemp.argtypes = [c_char_p]
DUMMYLIB_so.mktemp.restype = c_char_p

# file /usr/include/stdlib.h, line 827, column 12
DUMMYLIB_so.mkstemp.argtypes = [c_char_p]
DUMMYLIB_so.mkstemp.restype = c_int

# file /usr/include/stdlib.h, line 849, column 12
DUMMYLIB_so.mkstemps.argtypes = [c_char_p, c_int]
DUMMYLIB_so.mkstemps.restype = c_int

# file /usr/include/stdlib.h, line 870, column 14
DUMMYLIB_so.mkdtemp.argtypes = [c_char_p]
DUMMYLIB_so.mkdtemp.restype = c_char_p

# file /usr/include/stdlib.h, line 923, column 12
DUMMYLIB_so.system.argtypes = [c_char_p]
DUMMYLIB_so.system.restype = c_int

# file /usr/include/stdlib.h, line 940, column 14
DUMMYLIB_so.realpath.argtypes = [c_char_p, c_char_p]
DUMMYLIB_so.realpath.restype = c_char_p

# file /usr/include/stdlib.h, line 948, column 15
__compar_fn_t = CFUNCTYPE(c_int, POINTER(None), POINTER(None))

# file /usr/include/stdlib.h, line 960, column 14
DUMMYLIB_so.bsearch.argtypes = [POINTER(None), POINTER(None), c_int, c_int, CFUNCTYPE(c_int, POINTER(None), POINTER(None))]
DUMMYLIB_so.bsearch.restype = POINTER(None)

# file /usr/include/stdlib.h, line 970, column 13
DUMMYLIB_so.qsort.argtypes = [POINTER(None), c_int, c_int, CFUNCTYPE(c_int, POINTER(None), POINTER(None))]
DUMMYLIB_so.qsort.restype = None

# file /usr/include/stdlib.h, line 980, column 12
DUMMYLIB_so.abs.argtypes = [c_int]
DUMMYLIB_so.abs.restype = c_int

# file /usr/include/stdlib.h, line 981, column 17
DUMMYLIB_so.labs.argtypes = [c_long]
DUMMYLIB_so.labs.restype = c_long

# file /usr/include/stdlib.h, line 984, column 36
DUMMYLIB_so.llabs.argtypes = [c_long]
DUMMYLIB_so.llabs.restype = c_long

# file /usr/include/stdlib.h, line 998, column 14
DUMMYLIB_so.div.argtypes = [c_int, c_int]
DUMMYLIB_so.div.restype = div_t

# file /usr/include/stdlib.h, line 1000, column 15
DUMMYLIB_so.ldiv.argtypes = [c_long, c_long]
DUMMYLIB_so.ldiv.restype = ldiv_t

# file /usr/include/stdlib.h, line 1004, column 30
DUMMYLIB_so.lldiv.argtypes = [c_long, c_long]
DUMMYLIB_so.lldiv.restype = lldiv_t

# file /usr/include/stdlib.h, line 1018, column 14
DUMMYLIB_so.ecvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
DUMMYLIB_so.ecvt.restype = c_char_p

# file /usr/include/stdlib.h, line 1024, column 14
DUMMYLIB_so.fcvt.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int)]
DUMMYLIB_so.fcvt.restype = c_char_p

# file /usr/include/stdlib.h, line 1030, column 14
DUMMYLIB_so.gcvt.argtypes = [c_double, c_int, c_char_p]
DUMMYLIB_so.gcvt.restype = c_char_p

# file /usr/include/stdlib.h, line 1036, column 14
DUMMYLIB_so.qecvt.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int)]
DUMMYLIB_so.qecvt.restype = c_char_p

# file /usr/include/stdlib.h, line 1039, column 14
DUMMYLIB_so.qfcvt.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int)]
DUMMYLIB_so.qfcvt.restype = c_char_p

# file /usr/include/stdlib.h, line 1042, column 14
DUMMYLIB_so.qgcvt.argtypes = [c_longdouble, c_int, c_char_p]
DUMMYLIB_so.qgcvt.restype = c_char_p

# file /usr/include/stdlib.h, line 1048, column 12
DUMMYLIB_so.ecvt_r.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int), c_char_p, c_int]
DUMMYLIB_so.ecvt_r.restype = c_int

# file /usr/include/stdlib.h, line 1051, column 12
DUMMYLIB_so.fcvt_r.argtypes = [c_double, c_int, POINTER(c_int), POINTER(c_int), c_char_p, c_int]
DUMMYLIB_so.fcvt_r.restype = c_int

# file /usr/include/stdlib.h, line 1055, column 12
DUMMYLIB_so.qecvt_r.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int), c_char_p, c_int]
DUMMYLIB_so.qecvt_r.restype = c_int

# file /usr/include/stdlib.h, line 1059, column 12
DUMMYLIB_so.qfcvt_r.argtypes = [c_longdouble, c_int, POINTER(c_int), POINTER(c_int), c_char_p, c_int]
DUMMYLIB_so.qfcvt_r.restype = c_int

# file /usr/include/stdlib.h, line 1068, column 12
DUMMYLIB_so.mblen.argtypes = [c_char_p, c_int]
DUMMYLIB_so.mblen.restype = c_int

# file /usr/include/stdlib.h, line 1071, column 12
DUMMYLIB_so.mbtowc.argtypes = [POINTER(c_int), c_char_p, c_int]
DUMMYLIB_so.mbtowc.restype = c_int

# file /usr/include/stdlib.h, line 1075, column 12
DUMMYLIB_so.wctomb.argtypes = [c_char_p, c_int]
DUMMYLIB_so.wctomb.restype = c_int

# file /usr/include/stdlib.h, line 1079, column 15
DUMMYLIB_so.mbstowcs.argtypes = [POINTER(c_int), c_char_p, c_int]
DUMMYLIB_so.mbstowcs.restype = c_int

# file /usr/include/stdlib.h, line 1083, column 15
DUMMYLIB_so.wcstombs.argtypes = [c_char_p, POINTER(c_int), c_int]
DUMMYLIB_so.wcstombs.restype = c_int

# file /usr/include/stdlib.h, line 1094, column 12
DUMMYLIB_so.rpmatch.argtypes = [c_char_p]
DUMMYLIB_so.rpmatch.restype = c_int

# file /usr/include/stdlib.h, line 1105, column 12
DUMMYLIB_so.getsubopt.argtypes = [POINTER(c_char_p), POINTER(c_char_p), POINTER(c_char_p)]
DUMMYLIB_so.getsubopt.restype = c_int

# file /usr/include/stdlib.h, line 1151, column 12
DUMMYLIB_so.getloadavg.argtypes = [c_int, c_int]
DUMMYLIB_so.getloadavg.restype = c_int

# file fast_mmap.c, line 6, column 16

class fmmap_st(Structure):
    pass
fmmap_st._align_ = 1
fmmap_st._fields_ = [('ptr', POINTER(None)), ('length', c_int)]

# file fast_mmap.c, line 9, column 3
fmmap_st = fmmap_st

# file fast_mmap.c, line 11, column 5
DUMMYLIB_so.fmmap_mmap.argtypes = [POINTER(None), c_int, c_int, c_int, c_int, c_long, POINTER(fmmap_st)]
DUMMYLIB_so.fmmap_mmap.restype = c_int

# file fast_mmap.c, line 21, column 5
DUMMYLIB_so.fmmap_unmap.argtypes = [fmmap_st]
DUMMYLIB_so.fmmap_unmap.restype = c_int

# file fast_mmap.c, line 25, column 5
DUMMYLIB_so.fmmap_write.argtypes = [fmmap_st, POINTER(None), c_int, c_int]
DUMMYLIB_so.fmmap_write.restype = c_int

# file fast_mmap.c, line 34, column 7
DUMMYLIB_so.fmmap_read.argtypes = [fmmap_st, c_int, c_int]
DUMMYLIB_so.fmmap_read.restype = c_char_p

# file fast_mmap.c, line 44, column 7
DUMMYLIB_so.fmmap_getptr.argtypes = [fmmap_st, c_int]
DUMMYLIB_so.fmmap_getptr.restype = POINTER(None)

# file fast_mmap.c, line 52, column 5
DUMMYLIB_so.fmmap_sync.argtypes = [fmmap_st, c_int]
DUMMYLIB_so.fmmap_sync.restype = c_int
