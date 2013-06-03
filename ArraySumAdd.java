/**
*  Given an array and a sum, determine if any two of the array elements add up to the sum.
**/

import java.util.*;

public class ArraySumAdd {

	public static boolean hasSum(int[] arr, int sum) {
		HashSet<Integer> h = new HashSet<Integer>();
		
		for(int i=0; i<arr.length; i++) {
			if(h.contains(sum - arr[i]))
				return true;
			h.add(arr[i]);
		}
		
		return false;
	}
}
