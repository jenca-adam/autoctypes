import re


def make_identifier(s):
    return re.sub(r"\W", "_", s)

def get_root_type(tp):
    if not getattr(tp, "_NEEDSDEF", None):
        return None
    while tp._NEEDSDEF!=True:
        tp=tp._NEEDSDEF
    return tp
