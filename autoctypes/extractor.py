"""
Extracts data from C header files
"""

import warnings
from clang import cindex
import os
from . import ctypes_ext
from .context import Context
from .util import make_identifier, get_root_type
from .clang_ext import is_function_inlined, CLANG_INCLUDE_PATH
from .code_generator import (
    CodeGenerator,
    StructCodeGenerator,
    FuncCodeGenerator,
    TypedefCodeGenerator,
)


def location_to_str(loc):
    """Converts a libclang location to a readable string"""
    if loc:
        return (
            f"file {getattr(loc.file,'name','<unknown file>')}, "
            f"line {loc.line}, column {loc.column}"
        )
    return "<unknown loc>"


class Extractor:
    """Extracts data from C header files"""

    def __init__(self, path, context, skip_includes=False):
        self.tu = cindex.TranslationUnit.from_source(
            path,
            args=[f"-I{CLANG_INCLUDE_PATH}", *context.cflags],
            options=cindex.TranslationUnit.PARSE_DETAILED_PROCESSING_RECORD,
        )
        self.cursor = self.tu.cursor
        self.context = context
        self.typedefs = {}
        self.structs = {}
        self.elaborated_cache = {}
        self.ctype_cache = {}
        self.processing = []
        self.skip_includes = skip_includes

        self.target_file = os.path.abspath(path)

    def extract_code_generators(self):
        """Generates CodeGenerators from a C header file"""
        cursor_handlers = {
            cindex.CursorKind.STRUCT_DECL: self._handle_cursor_mk_code_generator,
            cindex.CursorKind.UNION_DECL: self._handle_cursor_mk_code_generator,
            cindex.CursorKind.TYPEDEF_DECL: self._handle_cursor_typedef,
            cindex.CursorKind.FUNCTION_DECL: self._handle_cursor_function,
        }
        for child in self.cursor.get_children():
            if self.skip_includes and child.location.file:
                child_file = os.path.abspath(child.location.file.name)
                if child_file != self.target_file:
                    continue
            handler = cursor_handlers.get(child.kind)

            if handler:
                if self.context.names and child.spelling not in self.context.names:
                    continue
                yield handler(child)

    def _handle_cursor_mk_code_generator(self, curs):
        return CodeGenerator.from_ctype(self.get_ctypes_type(curs=curs), self.context)

    def _handle_cursor_typedef(self, curs):
        return TypedefCodeGenerator(
            self.get_ctypes_type(
                curs.type.get_canonical(), loc=curs.location, curs=curs
            ),
            curs.spelling,
            self.context,
            location_to_str(curs.location),
        )

    def _handle_cursor_function(self, curs):
        return FuncCodeGenerator(self.get_ctypes_type(curs=curs), self.context)

    def get_ctypes_type(self, tp=None, /, loc=None, curs=None):
        """Converts a libclang type to a ctypes type"""
        if not curs and not tp:
            raise ValueError("specify either tp or curs")
        tp = tp or curs.type
        if curs and curs in self.ctype_cache:
            return self.ctype_cache[curs]  # cursors are hashable, but types aren't.
            # could've hashed the c struct content?
            # probably doesn't matter

        loc = loc or (curs.location if curs else None)

        type_handlers = {
            cindex.TypeKind.BOOL: self._handle_type_primitive,
            cindex.TypeKind.CHAR16: self._handle_type_primitive,
            cindex.TypeKind.CHAR32: self._handle_type_primitive,
            cindex.TypeKind.CHAR_S: self._handle_type_primitive,
            cindex.TypeKind.CHAR_U: self._handle_type_primitive,
            cindex.TypeKind.COMPLEX: self._handle_type_primitive,
            cindex.TypeKind.DOUBLE: self._handle_type_primitive,
            cindex.TypeKind.FLOAT: self._handle_type_primitive,
            cindex.TypeKind.FLOAT128: self._handle_type_primitive,
            cindex.TypeKind.HALF: self._handle_type_primitive,
            cindex.TypeKind.INT: self._handle_type_sized_int,
            cindex.TypeKind.INT128: self._handle_type_primitive,
            cindex.TypeKind.LONG: self._handle_type_sized_int,
            cindex.TypeKind.LONGDOUBLE: self._handle_type_primitive,
            cindex.TypeKind.LONGLONG: self._handle_type_sized_int,
            cindex.TypeKind.SCHAR: self._handle_type_primitive,
            cindex.TypeKind.SHORT: self._handle_type_primitive,
            cindex.TypeKind.UCHAR: self._handle_type_primitive,
            cindex.TypeKind.UINT: self._handle_type_sized_uint,
            cindex.TypeKind.UINT128: self._handle_type_primitive,
            cindex.TypeKind.ULONG: self._handle_type_sized_uint,
            cindex.TypeKind.ULONGLONG: self._handle_type_sized_uint,
            cindex.TypeKind.USHORT: self._handle_type_primitive,
            cindex.TypeKind.WCHAR: self._handle_type_primitive,
            cindex.TypeKind.CONSTANTARRAY: self._handle_type_array,
            cindex.TypeKind.VARIABLEARRAY: self._handle_type_array,
            cindex.TypeKind.INCOMPLETEARRAY: self._handle_type_array,
            cindex.TypeKind.POINTER: self._handle_type_pointer,
            cindex.TypeKind.ENUM: self._handle_type_enum,
            cindex.TypeKind.RECORD: self._handle_type_record,
            cindex.TypeKind.FUNCTIONPROTO: self._handle_type_functionproto,
            cindex.TypeKind.FUNCTIONNOPROTO: self._handle_type_functionproto,  # ???
            cindex.TypeKind.ELABORATED: self._handle_type_elaborated,
            cindex.TypeKind.INVALID: self._handle_type_invalid,
            cindex.TypeKind.VOID: self._handle_type_primitive,
            cindex.TypeKind.TYPEDEF: self._handle_type_elaborated,
        }

        handler = type_handlers.get(tp.kind, self._handle_type_unknown)
        ctp = handler(tp, loc, curs)
        if curs:
            self.ctype_cache[curs] = ctp
        return ctp

    def _handle_type_sized_int(self, tp, *_):
        mapping = {
            2: ctypes_ext.c_int16_FORCE,
            4: ctypes_ext.c_int32_FORCE,
            8: ctypes_ext.c_int64_FORCE,
        }
        return mapping.get(tp.get_size(), ctypes_ext.c_int32_FORCE)

    def _handle_type_sized_uint(self, tp, *_):
        mapping = {
            2: ctypes_ext.c_uint16_FORCE,
            4: ctypes_ext.c_uint32_FORCE,
            8: ctypes_ext.c_uint64_FORCE,
        }
        return mapping.get(tp.get_size(), ctypes_ext.c_uint32_FORCE)

    def _handle_type_primitive(self, tp, *_):
        mapping = {
            cindex.TypeKind.BOOL: ctypes_ext.c_bool,
            cindex.TypeKind.CHAR16: ctypes_ext.c_uint16_FORCE,
            cindex.TypeKind.CHAR32: ctypes_ext.c_uint32_FORCE,
            cindex.TypeKind.CHAR_S: ctypes_ext.c_char,
            cindex.TypeKind.CHAR_U: ctypes_ext.c_ubyte,
            cindex.TypeKind.COMPLEX: ctypes_ext.c_float_complex,
            cindex.TypeKind.DOUBLE: ctypes_ext.c_double,
            cindex.TypeKind.FLOAT: ctypes_ext.c_float,
            cindex.TypeKind.FLOAT128: ctypes_ext.c_float128,
            cindex.TypeKind.HALF: ctypes_ext.c_half,
            cindex.TypeKind.INT: ctypes_ext.c_int,
            cindex.TypeKind.INT128: ctypes_ext.c_int128,
            cindex.TypeKind.LONG: ctypes_ext.c_long,
            cindex.TypeKind.LONGDOUBLE: ctypes_ext.c_longdouble,
            cindex.TypeKind.LONGLONG: ctypes_ext.c_longlong,
            cindex.TypeKind.SCHAR: ctypes_ext.c_byte,
            cindex.TypeKind.SHORT: ctypes_ext.c_short,
            cindex.TypeKind.UCHAR: ctypes_ext.c_ubyte,
            cindex.TypeKind.UINT: ctypes_ext.c_uint,
            cindex.TypeKind.UINT128: ctypes_ext.c_uint128,
            cindex.TypeKind.ULONG: ctypes_ext.c_ulong,
            cindex.TypeKind.ULONGLONG: ctypes_ext.c_ulonglong,
            cindex.TypeKind.USHORT: ctypes_ext.c_ushort,
            cindex.TypeKind.WCHAR: ctypes_ext.c_wchar,
            cindex.TypeKind.VOID: None,
        }
        return mapping.get(tp.kind)

    def _handle_type_array(self, tp, loc, *_):
        size = tp.get_array_size()
        el_tp = self.get_ctypes_type(tp.get_array_element_type(), loc=loc)
        return ctypes_ext.mk_array(el_tp, max(size, 0))

    def _handle_type_pointer(self, tp, loc, curs):
        pointee = tp.get_pointee()
        if pointee.kind == cindex.TypeKind.CHAR_S:
            return ctypes_ext.c_char_p
        pointee_type = self.get_ctypes_type(pointee, loc=loc, curs=curs)
        if pointee.kind == cindex.TypeKind.FUNCTIONPROTO:
            return pointee_type

        return ctypes_ext.mk_ptr(pointee_type)

    def _handle_type_enum(self, tp, loc, _):
        curs = tp.get_declaration()
        return self.get_ctypes_type(curs.enum_type, loc=loc, curs=curs)

    def _handle_type_record(self, tp, loc, curs):
        name = make_identifier(tp.spelling.split()[-1].strip())
        self.context._renamed[tp.spelling] = name
        align = tp.get_align() if curs else 0
        is_union = tp.get_declaration().kind == cindex.CursorKind.UNION_DECL
        loc = loc or tp.get_declaration().location
        # print(tp.get_declaration().kind, is_union)
        fielditer = list(
            chld
            for chld in (curs.get_children() if curs else tp.get_fields())
            if chld.kind == cindex.CursorKind.FIELD_DECL
            or chld.is_anonymous_record_decl()
        )
        self.processing.append(tuple(tp.data))
        fields = [
            (
                make_identifier(
                    "_" + field.spelling
                    if field.is_anonymous_record_decl()
                    else field.spelling
                ),
                self.get_ctypes_type(curs=field),
            )
            for field in fielditer
        ]
        for index, field in enumerate(fielditer):
            width = field.get_bitfield_width()
            if width > 0:
                fields[index] = (*fields[index], width)

        self.processing.pop()
        anon = [
            make_identifier(
                "_" + field.spelling
                if field.is_anonymous_record_decl()
                else field.spelling
            )
            for field in fielditer
            if field.is_anonymous_record_decl()
        ]
        localdefs = []
        for index, (spelling, ctp, *bw) in enumerate(fields):
            needsdef = get_root_type(ctp)
            if needsdef:
                localdefs.append(CodeGenerator.from_ctype(needsdef, self.context))
                fields[index] = (
                    spelling,
                    (
                        ctp
                        if issubclass(ctp, ctypes_ext.EPOINTER)
                        or issubclass(ctp, ctypes_ext.EARRAY)
                        else ctypes_ext.mk_elaborated(needsdef.__qualname__, needsdef)
                    ),
                    *bw,
                )  # not _handle_type_elaborated because of the canonical check
        return ctypes_ext.make_struct(
            name,
            fields,
            align,
            location_to_str(loc),
            localdefs,
            is_union,
            self.context,
            anon,
        )

    def _handle_type_functionproto(self, tp, loc, curs):
        restype = self.get_ctypes_type(tp.get_result(), loc=loc)
        argtypes = []
        argnames = []
        orig_argnames = []
        if tp.kind != cindex.TypeKind.FUNCTIONNOPROTO:
            if not curs:
                argtypes = [
                    self.get_ctypes_type(arg, loc=loc) for arg in tp.argument_types()
                ]
                argnames = [f"arg{i+1}" for i in range(len(argtypes))]
            else:
                index = 1
                for child in curs.get_children():
                    if child.kind != cindex.CursorKind.PARM_DECL:
                        continue
                    argtypes.append(
                        self.get_ctypes_type(child.type, child.location, child)
                    )
                    argnames.append(make_identifier(child.spelling) or f"arg{index}")
                    orig_argnames.append(child.spelling)
                    index += 1
        inline = False
        variadic = tp.is_function_variadic()
        func_name = make_identifier(curs.spelling) if curs else "ANONYMOUS"

        if curs:
            self.context._renamed[curs.spelling] = func_name
            inline = bool(is_function_inlined(curs))
        localdefs = []
        for tp in (*argtypes, restype):
            needsdef = get_root_type(tp)
            if needsdef:
                localdefs.append(CodeGenerator.from_ctype(needsdef, self.context))

        if inline:
            return ctypes_ext.make_inline_func(
                func_name,
                restype,
                argtypes,
                argnames,
                orig_argnames,
                self,
                localdefs,
                variadic,
                list(curs.get_children()),
                location_to_str(loc),
                self.context,
            )
        return ctypes_ext.make_func(
            func_name,
            restype,
            argtypes,
            argnames,
            localdefs,
            variadic,
            location_to_str(loc),
            self.context,
        )

    def _handle_type_elaborated(self, tp, loc, *_):
        if tp.spelling not in self.typedefs:
            canon = tp.get_canonical()
            if tuple(canon.data) in self.processing:
                return ctypes_ext.mk_elaborated(tp.spelling, None)
            elif canon.kind != cindex.TypeKind.ELABORATED:
                data = tuple(canon.data)
                if data not in self.elaborated_cache:
                    self.processing.append(data)
                    self.elaborated_cache[data] = self.get_ctypes_type(canon)
                    self.processing.pop()
                return self.elaborated_cache[data]
            else:
                warnings.warn(
                    UserWarning(
                        f"{location_to_str(loc)}: "
                        f"elaborated type {tp.spelling} not in typedefs. Using int."
                    )
                )
            return ctypes_ext.c_int
        return ctypes_ext.mk_elaborated(
            tp.spelling, self.typedefs.get(tp.spelling, ctypes_ext.c_int)
        )

    def _handle_type_invalid(self, tp, loc, *_):
        warnings.warn(
            UserWarning(
                f"{location_to_str(loc)}: invalid type: {tp.spelling}. Using int."
            )
        )
        return ctypes_ext.c_int

    def _handle_type_unknown(self, tp, loc, *_):
        warnings.warn(
            UserWarning(
                f"{location_to_str(loc)}: unsupported type: {tp.kind}. Using int."
            )
        )
        return ctypes_ext.c_int
