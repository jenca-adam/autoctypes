from clang import cindex
import ast


class Translator:
    def __init__(self, inline_func):
        self.inline_func = inline_func
        self.body = []

    def get_py_ast(self):
        return [ast.Pass(), ast.Name("#TODO")]  # TODO
