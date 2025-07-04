import autoctypes

extractor = autoctypes.extractor.Extractor(
    "fast_mmap.c", autoctypes.context.Context([], [])
)
first_type = next(extractor.cursor.get_children())
for gen in extractor.extract_code_generators():
    print(autoctypes.reconstruct.stringify_code_generator(gen))
