#include <stdio.h>
#include <stdlib.h>

struct Node {
	int data;
	struct Node *next;
};

int findMiddle(int prevNodes, struct Node *head, struct Node **mid, int *found) {
	int nextNodes;
	
	if(!head) {
		return 0;
	}
	
	nextNodes = findMiddle(prevNodes + 1, head->next, mid, found);
	if(nextNodes == prevNodes || (nextNodes > prevNodes && !*found)) {
		*mid = head;
		*found = 1;
	}
	
	printf("At node %d, prevNodes == %d, nextNodes == %d\n", head->data, prevNodes, nextNodes);
	return nextNodes + 1;
}

int main() {
	int fnd;
	struct Node *A;
	struct Node *B;
	struct Node *C;
	struct Node *D;
	struct Node *E;
	struct Node *res;
	struct Node *mid;
	
	A = malloc(sizeof(struct Node));
	B = malloc(sizeof(struct Node));
	C = malloc(sizeof(struct Node));
	D = malloc(sizeof(struct Node));
	E = malloc(sizeof(struct Node));
	
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
	printf("\nMiddle node's data: %d", mid->data);
	
}
