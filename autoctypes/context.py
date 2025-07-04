"""
Defines a class that stores the context autoctypes has been invoked in.
"""

from .util import make_identifier


class Library:
    def __init__(self, name):
        self.id = make_identifier(name)
        self.name = name


class Context:
    """dummy"""

    def __init__(self, files, libs):
        self.comment = True

    def find_lib(self, func):
        # TODO
        return Library("DUMMYLIB.so")
