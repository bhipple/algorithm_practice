#include <stdio.h>
#include <stdlib.h>

struct node {
    int data;
    struct node *left;
    struct node *right;
};

struct node* secondLargest(struct node* head) {
    if(!head) return NULL;

    // If there is no right subtree, then the second largest node
    // is the rightmost node of the left subtree
    if(!head->right) {
        head = head->left;
        while(head && head->right) {
            head = head->right;
        }
        return head;
    }

    while(head->right->right) {
        head = head->right;
    }
    // If the rightmost node does not have a left subtree,
    // then head is the second largest node
    if(!head->right->left) {
        return head;
    }

    head = head->right->left;
    while(head->right) {
        head = head->right;
    }
    return head;
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

    // Run on the whole tree
    printf("Value of second largest node is: %d (Expecting 192)\n", secondLargest(&A)->data);

    // Run on the subtree rooted at 256
    printf("Value of second largest node is: %d (Expecting 192)\n", secondLargest(&C)->data);

    // Run on the subtree rooted at 64
    printf("Value of second largest node is: %d (Expecting 48)\n", secondLargest(&B)->data);

    // Run on the subtree rooted at 32
    printf("Value of second largest node is: %d (Expecting 32)\n", secondLargest(&D)->data);
}
