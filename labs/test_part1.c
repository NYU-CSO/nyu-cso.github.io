#include <stdio.h>

// you have to declare the array_sum function signature here, otherwise, the compiler would complain
// The function is defined in part1.c
extern int array_sum(int *a, int n);


int
main() {
	// this is the simplest test;
	int array[5] = {1, 2, 3, 4, 5};
	int sum;
        sum = array_sum(array, 5);
	printf("sum is %d\n", sum);

	// this is a more sophisticated test
	int array2[100];
	sum = 0;
	for (int i = 0; i < 100; i++) {
		array2[i] = i;
		sum += i;
		int calculated = array_sum(array2, i+1);
		if (calculated != sum) {
			printf("The sum is calculated incorrectly! %d != %d(expected)\n", calculated, sum);
		}
	}
	printf("all my tests are good!\n");
}
