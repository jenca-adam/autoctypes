import autoctypes
import sys
extractor = autoctypes.extractor.Extractor(
    "/usr/include/linux/videodev2.h", autoctypes.context.Context([], []), True
)
first_type = next(extractor.cursor.get_children())
taken = set()
for gen in extractor.extract_code_generators():
    print(autoctypes.reconstruct.stringify_code_generator(gen, taken=taken))
    print(taken, file=sys.stderr)
