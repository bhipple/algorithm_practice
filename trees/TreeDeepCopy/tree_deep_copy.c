#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left;
    struct node *right;
};

struct node* deepcopy(struct node* head) {
    if(!head) return NULL;

    struct node* cpy = malloc(sizeof(struct node));
    cpy->data = head->data;

    cpy->left = deepcopy(head->left);
    cpy->right = deepcopy(head->right);

    return cpy;
}


// ============================================================================
//                                  Testing
// ============================================================================
void printInOrder(struct node* head) {
    if(!head) return;
    printInOrder(head->left);
    printf("%d\n", head->data);
    printInOrder(head->right);
}

void incTree(struct node* head) {
    if(!head) return;
    ++head->data;
    incTree(head->left);
    incTree(head->right);
}

int main() {
    struct node A, B, C, D, E;
    A.data = 128;
    B.data = 64;
    C.data = 256;
    D.data = 32;
    E.data = 48;

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

    struct node* cpyTree = deepcopy(&A);
    incTree(cpyTree);

    // Copy tree should be 1 larger than original in all node values
    printInOrder(&A);
    printf("\n");
    printInOrder(cpyTree);
}
