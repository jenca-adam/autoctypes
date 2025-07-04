import ctypes
import ctypes.util
import warnings
import sys


def libload(libname):
    if sys.platform in ["linux", "darwin"]:

        return ctypes.CDLL(ctypes.util.find_library(libname))
    if sys.platform == "win32":
        return ctypes.CDLL(ctypes.util.find_library(f"{libname}.dll"))
    raise RuntimeError(f"unsupported OS: {sys.platform}")
