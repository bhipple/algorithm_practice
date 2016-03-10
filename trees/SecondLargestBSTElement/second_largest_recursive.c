#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left;
    struct node *right;
};

// Doing a reverse in-order tree traversal
void secondLargest(struct node* head, int* visited, struct node** res) {
    if(!head) return;

    // Right subtree
    secondLargest(head->right, visited, res);

    // This node
    *visited += 1;
    if(*visited == 2) {
        *res = head;
        return;
    } else if(*visited > 2) {
        return;
    }

    // Left subtree
    secondLargest(head->left, visited, res);
}

int main() {
    struct node A, B, C, D, E, F;
    A.data = 128;
    B.data = 64;
    C.data = 256;
    D.data = 32;
    E.data = 48;
    F.data = 192;

    A.left = &B;
    A.right = &C;
    B.left = &D;
    B.right = 0;
    C.left = &F;
    C.right = 0;
    D.left = 0;
    D.right = &E;
    E.left = 0;
    E.right = 0;
    F.left = 0;
    F.right = 0;

    /*

              128
        64          256
    32           192
      48

    */

    struct node* res = malloc(sizeof(struct node));
    int* visited = malloc(sizeof(int));

    // Run on the whole tree
    *visited = 0;
    secondLargest(&A, visited, &res);
    printf("Value of second largest node is: %d (Expecting 192)\n", res->data);

    // Run on the subtree rooted at 256
    *visited = 0;
    secondLargest(&C, visited, &res);
    printf("Value of second largest node is: %d (Expecting 192)\n", res->data);

    // Run on the subtree rooted at 64
    *visited = 0;
    secondLargest(&B, visited, &res);
    printf("Value of second largest node is: %d (Expecting 48)\n", res->data);

    // Run on the subtree rooted at 32
    *visited = 0;
    secondLargest(&D, visited, &res);
    printf("Value of second largest node is: %d (Expecting 32)\n", res->data);
}
