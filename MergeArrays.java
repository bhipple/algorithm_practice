/**
* Merge 2 sorted arrays of equal length, where A has a large enough buffer at the end to hold B.  
**/

public int[] mergeArrays(int[] A, int[] B) {
  int pA = B.length - 1;
	int pB = B.length - 1;
	int pX = A.length - 1;
	
	while(pA >= 0 && pB >= 0) {
		if(A[pA] > B[pB]) {
			A[pX] = A[pA];
			pA--;
			pX--;
		}
		else {
			A[pX] = B[pB];
			pB--;
			pX--;
		}
	}
	
	while(pB >= 0) {
		A[pX] = B[pB];
		pX--;
		pB--;
	}
}
