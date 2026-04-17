from clang import cindex
import ast
import traceback

class Translator:
    def __init__(self, inline_func, context):
        self.inline_func = inline_func
        self.extractor = inline_func._extractor
        self.ctx = context
        self.body = []
        self.needs = []
    def print_ast(self, node, indent=0):
        print(f"{' '*indent}{node.kind} {node.spelling!r}")
        for child in node.get_children():
            self.print_ast(child, indent + 1)
   
    def translate(self, node):
        handlers = {
            cindex.CursorKind.COMPOUND_STMT: self._translate_compound_stmt,
            cindex.CursorKind.RETURN_STMT: self._translate_return_stmt,
            cindex.CursorKind.CALL_EXPR: self._translate_call_expr
        }
        handler = handlers.get(node.kind)
        if not handler:
            return
        yield from handler(node)
    def _translate_compound_stmt(self, node):
        # just chain it together
        for child in node.get_children():
            yield from self.translate(child)
    def _translate_return_stmt(self, node):
        kids = list(node.get_children())
        if not kids:
            yield ast.Return()
        try:
            result = next(self.translate(kids[0]))
            yield ast.Return(value=result)
        except StopIteration:
            yield ast.Return()
    def _translate_call_expr(self, node):
        func_name = node.spelling
        
        ### 
    def get_py_ast(self):
        for node in self.inline_func._body:
            if node.kind!=cindex.CursorKind.COMPOUND_STMT:
                continue
            self.print_ast(node)
            try:
                
                self.body.extend(self.translate(node))
            except Exception as e:
                traceback.print_exc()
                self.body = [ast.Pass(), ast.Name(f" #FIXME: {str(e)}")]
        try:
            ast.parse(ast.unparse(ast.FunctionDef(name="a",body=self.body, args=ast.arguments(), lineno=0)))
        except Exception as e:
            self.body = [ast.Pass(), ast.Name(f" #FIXME: {str(e)}")]
        return self.body
