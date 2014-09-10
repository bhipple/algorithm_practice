#include <stdio.h>
#include <stdlib.h>

char* removeCommans(char* num);
const int LIMIT = 64;

char* removeCommas(char* num) {
    char *t, *c;

    c = &num[0];
    t = c;
    while(*c != '\0') {
        if(*c != ',') {
            *t = *c;
            t++;
        }
        c++;
    }
    *t = '\0';
    return num;
}

// Tester
int main()
{
    char* num = malloc(LIMIT);
    printf("Enter a string with commas (number format): \n");
    scanf("%s", num);

    removeCommas(num);
    printf("Final string:\t%s\n", num);
}
