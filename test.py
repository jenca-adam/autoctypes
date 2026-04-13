import autoctypes
import sys
import ctypes

extractor = autoctypes.extractor.Extractor(
    "/usr/include/vulkan/vulkan.h",
    autoctypes.context.Context([], [autoctypes.context.Library("libvulkan.so")]),
    False,
)
first_type = next(extractor.cursor.get_children())
taken = set()
for gen in extractor.extract_code_generators():
    print(
        autoctypes.reconstruct.stringify_code_generator(
            gen, taken=taken, type_hints=True
        )
    )
