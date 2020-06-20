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


void np_array_2dim(const int m, const int n, const double **x, double **y)
{
	size_t i, j;

	for(i=0; i<m; i++)
		for(j=0; j<n; j++)
			y[i][j] = x[i][j]+1;
}


void np_array_3dim(const int m, const int n, const int o, const double *x, double *y)
{
	size_t i, j, k;

	// printf("(m, n, o)=(%d, %d, %d)\n", m, n, o);
	for(i=0; i<m; i++){
		for(j=0; j<n; j++){
			for(k=0; k<o; k++){
				y[i*m*n+j*n+k] = x[i*m*n+j*n+k] + 1;
			}
		}
	}
}


void np_array_3dim_3ptr(const int m, const int n, const int o, const double ***x, double ***y)
{
	size_t i, j, k;

	// printf("(m, n, o)=(%d, %d, %d)\n", m, n, o);
	for(i=0; i<m; i++){
		for(j=0; j<n; j++){
			for(k=0; k<o; k++){
				y[i][j][k] = x[i][j][k] + 1;
			}
		}
	}
}

void np_array_3dim_3ptr_xx(const int m, const int n, const int o, const double ***x)
{
	size_t i, j, k;

	// printf("(m, n, o)=(%d, %d, %d)\n", m, n, o);
	for(i=0; i<m; i++){
		for(j=0; j<n; j++){
			for(k=0; k<o; k++){
				printf("%f, ", x[i][j][k]);
			}
			printf("\n");
		}
		printf("\n");
	}
}
