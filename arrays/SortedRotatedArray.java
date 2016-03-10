/**
 * Given a sorted array which is rotated n number of times. 
 * Find out how many times the array is rotated. Time complexity should be less than O(n).
 * 
 * @author Ben
 *
 */

public class SortedRotatedArray {
	
	private static int binarySearch(int[] arr, int left, int right)
	{
		int mid = (left + right) / 2;
		
		// base cases
		if(right < left)
			return -1;
		if(arr[mid-1] > arr[mid])
			return mid;
		
		// discontinuity on the right side
		if(arr[right] < arr[mid])
			return binarySearch(arr, mid+1, right);
		
		// discontinuity on the left side
		if(arr[left] > arr[mid]) 
			return binarySearch(arr, left+1, mid);
		
		return 0;
	}

}
