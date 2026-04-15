import re
import keyword

def make_identifier(s):
    ident = re.sub(r"\W", "_", s)
    if keyword.iskeyword(ident):
        ident=ident+"_" # potential name clash?
    return ident


def get_root_type(tp):
    if not getattr(tp, "_NEEDSDEF", None):
        return None
    while tp._NEEDSDEF != True:
        tp = tp._NEEDSDEF
    return tp
