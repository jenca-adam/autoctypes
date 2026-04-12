struct anon_test{
    int a;
    union {
        int b;
        int c;
    };
    union {
        int d;
        int e;
    } f;
};

struct q{
    struct anon_test r[69];
};
