"""
Defines a class that stores the context autoctypes has been invoked in.
"""

from .util import make_identifier
from .libload import libload


class Library:
    def __init__(self, name, id=None):
        self.id = id or make_identifier(name)
        self.name = name
        self.dll = libload(name)


class Context:
    def __init__(
        self,
        files,
        libs,
        comment=True,
        type_hints=True,
        fluff=True,
        names=set(),
        wrapper_funcs=True,
    ):
        self.comment = comment
        self.type_hints = type_hints
        self.files = files
        self.libs = libs
        self.fluff = fluff
        self.wrapper_funcs = wrapper_funcs
        self.names = set(names)
        self._taken_names = set()

    def find_lib(self, func):
        for lib in self.libs:
            try:
                lib.dll[func]
                return lib
            except AttributeError:
                continue
