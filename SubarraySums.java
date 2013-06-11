/**
** Given an array, subarray size k and a number sum, find the number of subarrays of size k that sum up to sum.
**/

import java.util.*;

public class SubarraySums {	
	public static int getNumSubArraysThatAddUpToSum(int[] arr, int k, int sum) {
		int res = 0;
		int tempSum = 0;
		
		for(int i=0; i<k; i++)
			tempSum += arr[i];
      
    if(tempSum == sum)
			res++;
		
		for(int j=k; j<arr.length; j++) {
			tempSum += arr[j];
			tempSum -= arr[j-k];
      
      if(tempSum == sum) 
				res++;
		}
		
		return res;
	}
}
