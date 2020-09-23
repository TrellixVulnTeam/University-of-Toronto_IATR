#include <stdio.h>
#include <stdlib.h>

void fun4(int *d) {
	d = malloc(sizeof(int));
	*d = 40;
}

void fun3(int **c) {
	*c = malloc(sizeof(int));
	**c = 30;
}

void fun2(int *b) {
	*b = 20; //b is int* of 1
}

void fun1(int a) {
	a = 10;
}

int main() {

	int x = 1;
	int *y = &x;
	int **z = &y;

	int num = 7;
  int *ptr = y;

    // Notice that fun1 changes only the value of parameter a, not x.
	printf("x before fun1(x): %d\n", x);
	fun1(x);
	printf("x after fun1(x): %d\n\n", x);

    // Notice that fun2 changes the value pointed to by y.
	printf("y before fun2(y): address %p holds value %d\n", y, *y);
	fun2(y);
	printf("y after fun2(y): address %p holds value %d\n\n", y, *y);

    // Notice here that the address of z doesn't change, but the address it
    // is pointing to does. The value of *z is assigned a pointer to an address on
    // the heap.
	printf("z before fun3(y): %p\n", z);
	printf("*z before fun3(y): %p\n", *z);
	printf("**z before fun3(y): %d\n", **z);
	fun3(z);
	printf("z after fun3(y): %p\n", z);
	printf("*z after fun3(y): %p\n", *z);
	printf("**z after fun3(y): %d\n\n", **z);

	// Can we have achieve what we did in fun3 with only a single pointer
	// instead of a pointer to pointer?
	// No, parameter d would point to the heap, but the
	// pointer declared in main would still be pointing to its original value.
	printf("ptr before fun4(y): address %p holds value %d\n", y, *y);
	fun4(ptr);
	printf("ptr after fun4(y): address %p holds value %d\n\n", y, *y);
}
