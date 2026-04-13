from ctypes import CDLL
from ctypes.util import find_library
import warnings
import sys


### TO BE INCLUDED IN THE GENERATED CODE
def _actp_libload(libname):
    if sys.platform in ["linux", "darwin"]:
        return CDLL(libname)
    if sys.platform == "win32":
        return CDLL(find_library(f"{libname.split('.')[0]}.dll"))
    raise RuntimeError(f"unsupported OS: {sys.platform}")


def libload(libname):
    return _actp_libload(libname)
