#include <stdio.h>
#include <stdlib.h>

// Pass-by-value vs. pass-by-reference example

void shouldIGoToSleep(int* sleepyTime) {
    *sleepyTime = 1;
}

int main(void) {
    printf("Is it bedtime?\n");

    int* sleepyTime = malloc(sizeof(int));
    shouldIGoToSleep(sleepyTime);

    if(*sleepyTime > 0) {
        printf("It's bedtime!\n");
    }
    else {
        printf("Nope, study moar.\n");
    }

    free(sleepyTime);
}
