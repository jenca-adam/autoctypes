inline int idk(int b){
    return b+1;
}
inline int twice(int a){return a*2;}
inline int mult(int a, int b){ return a*b;}
inline int apply1(int a){
    return idk(a);
}
inline int apply2(int in, int (*func)(int)){return (func)(in);};
inline int func_cast(int a, void *func){
    return ((int (*)(int))(func))(0);
}
