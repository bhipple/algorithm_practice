import java.util.*;

/**
 * Given an int[] of prime numbers, remove all duplicate primes.
 * @author Ben
 *
 */
public class RemoveDuplicatePrimes {
	
	public static int[] removeDuplicates(int[] arr) {
		long product = 1;
	
		for(int i=0; i<arr.length; i++) {
			if((product % arr[i] == 0)) {
				arr[i] = 0;
			}
			else
				product = product * arr[i];
		}
		
		// Move the deleted duplicates to the end of the array, so we don't have to create a new array
		// (although the return array will have some 0s at the end in return for this performance improvement
		int end = arr.length - 1;
		while(arr[end] == 0)
			end--;
		for(int i=0; i<arr.length; i++) {
			if(arr[i] == 0 && i < end) {
				arr[i] = arr[end];
				arr[end] = 0;
				while(arr[end] == 0)
					end--;
			}
		}
		return arr;
	}
}
