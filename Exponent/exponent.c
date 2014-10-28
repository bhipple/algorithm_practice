#include <stdio.h>
#include <stdlib.h>

// @assumption: b >= 0, p >= 1
int exponent(int b, int p) {
    if(b == 0) return 0;
    if(p == 0) return 1;

    int half = exponent(b, p/2);

    if(p % 2) return b * half * half;

    return half * half;
}

int main() {
    int b, p;
    printf("Enter a base: \n");
    scanf("%d", &b);

    printf("Enter an exponent: \n");
    scanf("%d", &p);

    printf("Result: %d\n", exponent(b, p));
}
