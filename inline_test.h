inline int add_const() {
    return 2 + 3;
}

inline int mixed_const() {
    return 10 - 4 * 2;
}

inline int nested_const() {
    return (1 + 2) * (3 + 4);
}
inline float float_const() {
    return 3.0 + 2.5;
}

inline float float_mix() {
    return (1.5 * 2.0) + 4.5;
}
inline int const_less() {
    return 2 < 3;
}

inline int const_equal() {
    return 5 == 5;
}

inline int const_not_equal() {
    return 7 != 8;
}
inline int const_and() {
    return (1 < 2) && (3 < 4);
}

inline int const_or() {
    return (1 > 2) || (3 < 4);
}
inline int const_bit_and() {
    return 6 & 3;
}

inline int const_bit_or() {
    return 4 | 1;
}

inline int const_bit_xor() {
    return 5 ^ 2;
}

inline int const_shift_left() {
    return 1 << 3;
}

inline int const_shift_right() {
    return 8 >> 2;
}
inline int const_int() {
    return 42;
}

inline float const_float() {
    return 3.14;
}

inline char const_char() {
    return 'Z';
}

inline const char* const_string() {
    return "hello world";
}
inline int* ptr_add_const() {
    return (int*)1000 + 2;
}

inline int* ptr_sub_const() {
    return (int*)2000 - 1;
}
inline int deep_expr() {
    return ((1 + 2) * (3 + 4)) - (5 << 1);
}
inline int chained_cmp() {
    return (1 < 2) == (3 < 4);
}
