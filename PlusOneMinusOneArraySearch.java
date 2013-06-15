/**
 * Given an array of integers such that each element is either +1 or -1 to its preceding element. 
 * Find 1st occurrence of a given number in that array without using linear search.
 * @author Ben
 *
 */

public class PlusOneMinusOneArraySearch {
	public static int find(int[] a, int target) {
		
		int res = 0;
		while(res < a.length && a[res] != target) {
			res = res + (Math.abs(target - a[res]));
		}
		
		if(a[res] == target)
			return res;
		else
			return -1;
	}
}
