#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;
struct Node {
    int data;
    Node *left;
    Node *right;
};

int children(Node* head) {
    if(!head) return 0;
    head->data = 1 + children(head->left) + children(head->right);
    return head->data;
}


// Tester
int main() {
    Node A, B, C, D, E;
    A.left = &B;
    A.right = &C;
    B.left = &D;
    B.right = 0;
    C.left = 0;
    C.right = 0;
    D.left = 0;
    D.right = &E;
    E.left = 0;
    E.right = 0;

    children(&A);
    printf("A has %d children\n", A.data);
}
