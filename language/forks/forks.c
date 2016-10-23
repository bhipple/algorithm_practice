#include <stdio.h>
#include <unistd.h>

// Question: How many times will 0, 1, and 2 each be printed?
// Run it for answer; `man fork` for details (for instance, the
// parent gets the child's pid in pid_t, while the child gets 0).

int main() {
    int i = 0;
    pid_t pid = 0;
    for(i = 0; i < 3; ++i) {
        pid = fork();
        printf("%d \t=>\t %d\n", pid, i);
    }
}
