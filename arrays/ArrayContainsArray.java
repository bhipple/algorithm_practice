/** 
*  Given two sorted arrays, check to see if either of them is a subarray of the other.
**/

public class ArrayContainsArray {
	public static boolean subArray(int[] a, int[] b) {
		if(a.length < b.length)
			return contains(a, b);
		else if(b.length < a.length)
			return contains(b, a);
		else //(a.length == b.length)
			return contains(a, b) || contains(b, a);
	}
	
	private static boolean contains(int[] a, int[] b) {
		int i = 0;
		int j = 0;
		while(i < a.length && j < b.length) {
			if(a[i] == b[j]) {
				i++;
				j++;
			}
			else if(a[i] > b[j]) {
				j++;
			}
			else if(a[i] < b[j])
				return false;
		}
		if(j > i)
			return false;
		else
			return true;
	}
}
