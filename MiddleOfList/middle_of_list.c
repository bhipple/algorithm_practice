#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};
typedef struct Node Node;

int findMiddle(int prevNodes, Node *head, Node **mid, int *found) {
    if(!head) return 0;

    int nextNodes = findMiddle(prevNodes + 1, head->next, mid, found);
    if(nextNodes == prevNodes || (nextNodes > prevNodes && !*found)) {
        *mid = head;
        *found = 1;
    }

    printf("At node %d, prevNodes == %d, nextNodes == %d\n", head->data, prevNodes, nextNodes);
    return nextNodes + 1;
}

int main() {
    int fnd;
    Node *A;
    Node *B;
    Node *C;
    Node *D;
    Node *E;
    Node *mid;

    A = malloc(sizeof(Node));
    B = malloc(sizeof(Node));
    C = malloc(sizeof(Node));
    D = malloc(sizeof(Node));
    E = malloc(sizeof(Node));

    A->next = B;
    B->next = C;
    C->next = D;
    D->next = E;

    A->data = 10;
    B->data = 20;
    C->data = 30;
    D->data = 40;
    E->data = 50;

    fnd = 0;

    fnd = findMiddle(0, A, &mid, &fnd);
    printf("\nMiddle node's data: %d\n", mid->data);

}
