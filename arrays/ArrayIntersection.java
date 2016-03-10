/**
**  Find the intersection of two arrays.
**/

import java.util.*;

public class ArrayIntersection {
  
	public static void main(String[] args) {
		int[] test = {1, 2, 3, 4};
		int[] testb = {3, 4, 5, 1, 6, 8, 12};
		
		int[] inter = intersection(test, testb);
		for(int i=0; i<inter.length; i++) 
			System.out.println(inter[i]);
	}

	public static int[] intersection(int[] A, int[] B) {
	
		Hashtable<Integer, Integer> h = new Hashtable<Integer, Integer>();
		
		for(int i=0; i<A.length; i++) {
			if(h.containsKey(A[i])) {
				int val = h.remove(A[i]);
				h.put(A[i], val+1);
			}
			else
				h.put(A[i],  1);
		}
		
		int[] intersect = new int[Math.min(A.length, B.length)];
		int ct = 0;
		for(int j=0; j<B.length; j++) {
			if(h.containsKey(B[j]) && h.get(B[j]) > 0) {
				int val = h.remove(B[j]);
				h.put(B[j],  val-1);
				
				intersect[ct] = B[j];
				ct++;
			}
		}
		
		int[] res = new int[ct];
		for(int i=0; i<ct; i++) {
			res[i] = intersect[i];
		}
		return res;
	}
	
}
