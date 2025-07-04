import re


def make_identifier(s):
    return re.sub(r"\W", "_", s)
