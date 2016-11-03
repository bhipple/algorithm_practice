#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

// Question: How many times will 0, 1, and 2 each be printed?
// Run it for answer; `man fork` for details (for instance, the
// parent gets the child's pid in pid_t, while the child gets 0).
void printingFork() {
    int i = 0;
    pid_t pid = 0;
    for(i = 0; i < 3; ++i) {
        pid = fork();
        printf("%d \t=>\t %d\n", pid, i);
    }
}

// Child processes don't get killed when parents die.
void lifetimes() {
    pid_t pid = fork();
    if(pid != 0) {
        printf("Parent process dying\n");
        exit(0);
    }

    for(int i = 0; i < 100; ++i) {
        printf("It's alive! ");
    }
}


int main() {
    //printingFork();
    lifetimes();
}
