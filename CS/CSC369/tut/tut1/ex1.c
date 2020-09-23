#include <stdio.h>

typedef struct {
    int a;
    int b;
} my_struct;

void foo1(my_struct x)
{
    x.a = 1;
    x.b = 1;
}

void foo2(my_struct *x)
{
    x->a = 2;
    x->b = 2;
}

void foo3(my_struct *x)
{
    my_struct y;
    y.a = 3;
    y.b = 3;
    x = &y;
}

int main()
{
    my_struct x = {10, 10};
    foo1(x);
    printf("%d, %d\n", x.a, x.b);

    foo2(&x);
    printf("%d, %d\n", x.a, x.b);

    foo3(&x);
    printf("%d, %d\n", x.a, x.b);
}
