#include <stdio.h>

int simple(char *str, int length) {
    printf("Calling simple with %s and %d\n", str, length);
    return 0;
}

int (*complex(int index))(char *s, int l) {
    printf("calling complex with %d\n", index);
    return simple;
}

int args(int(*f)(char *s, int r), int p) {
    f("args", 10);
    printf("Just called f in args\n");
    return p;
}

int main() {
    int (*x)(char *s, int l) = simple;
    x("main", 10);
    simple("main-simple", 20);

    int (*y)(char *s, int z) = complex(2);
    y("Phew", 30);

    return 0;
}
