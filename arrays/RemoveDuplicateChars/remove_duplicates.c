#include <stdio.h>
#include <stdlib.h>

void removeDuplicates(char* str);
const int LIMIT = 256;

void removeDuplicates(char* str) {
    char *t, *a;
    int hash[256];

    for(unsigned int i = 0; i < sizeof(hash)/sizeof(hash[0]); ++i) {
        hash[i] = 0;
    }

    a = &str[0];
    t = a;
    while(*a != '\0') {
        if(!hash[*a - 0]) {
            ++hash[*a - 0];
            *t = *a;
            t++;
        }
        a++;
    }
    *t = '\0';
}

// Tester
int main()
{
    char* str = malloc(LIMIT);
    printf("Enter a string with commas (number format): \n");
    scanf("%s", str);

    removeDuplicates(str);
    printf("Final string:\t%s\n", str);
}
