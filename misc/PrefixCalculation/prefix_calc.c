#include <stdio.h>

typedef struct Node Node;
struct Node {
    char data;
    Node *left;
    Node *right;
};

int calculate(Node *head) {
  if(!head)
      return 0;
  if(head->data == '+') {
      printf("Operator + found\n");
      return calculate(head->left) + calculate(head->right);
  } else if(head->data == '*') {
      printf("Operator * found\n");
      return calculate(head->left) * calculate(head->right);
  } else {
      printf("Data value %d found\n", head->data - '0');
      return head->data - '0';
  }
}


int main(void) {
    // Basic test case:
    //       +
    //     *    5
    //   3   6
    //
    //  Epxecting: (3 * 6) + 5 = 23

    Node A, B, C, D, E;
    A.data = '+';
    A.left = &B;
    A.right = &C;

    B.data = '*';
    B.left = &D;
    B.right = &E;

    C.data = '5';
    C.left = NULL;
    C.right = NULL;

    D.data = '3';
    D.left = NULL;
    D.right = NULL;

    E.data = '6';
    E.left = NULL;
    E.right = NULL;


    printf("\n%d\n", calculate(&A));
}
