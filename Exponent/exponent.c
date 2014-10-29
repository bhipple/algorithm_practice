#include <stdio.h>
#include <stdlib.h>

// @assumption: p >= 1
int exponent(int b, int p) {
    if(p < 1) return -1; // ERROR
    if(b == 0) return 0;
    if(p == 0) return 1;

    int half = exponent(b, p/2);

    if(p % 2) return b * half * half;

    return half * half;
}

int main() {
    int b, p;
    while(1) {
        printf("Enter a base: \n");
        scanf("%d", &b);

        printf("Enter an exponent: \n");
        scanf("%d", &p);

        printf("Result: %d\n\n\n", exponent(b, p));
    }
}
