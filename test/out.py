from ctypes import *


class test_c_3_5_(Union):
    pass


test_c_3_5_._align_ = 4
test_c_3_5_._fields_ = [("b", c_int), ("c", c_int)]
# file test.c, line 1, column 8


class anon_test(Structure):
    pass


anon_test._align_ = 4
anon_test._anonymous_ = ("union__anonymous_at_test_c_3_5_",)
anon_test._fields_ = [("a", c_int), ("union__anonymous_at_test_c_3_5_", test_c_3_5_)]
