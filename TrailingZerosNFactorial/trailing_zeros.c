#include <stdio.h>
#include <stdlib.h>

int trailing(int n) {
    int res = 0;
    int ct = n / 5;
    while(ct) {
        res += ct;
        ct /= 5;
    }

    return res;
}

// Tester
int main() {
    int n;
    while(1) {
        printf("Enter n: \n");
        scanf("%d", &n);

        printf("Result: %d\n\n\n", trailing(n));
    }
}
