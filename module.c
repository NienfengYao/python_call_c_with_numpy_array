/* 
	gcc -fPIC -shared -o module.so module.c
*/

#include <stdio.h>

int square(int i) {
	return i * i;
}


/* y = x+1. x/y are np array of 1-dim */
void np_array_1dim(double *x, size_t s, double *y) {
	unsigned int i;

	for (i=0; i < s; i++) {
		y[i] = x[i]+1;
	}
}
