/**
 * Given an array with all integers from 1 to 100, but with one integer missing and one integer doubled, find the missing integer
 * @author Ben
 *
 */
public class FindMissingNum {
	public static int findMissing(int[] arr) {
		boolean[] seen = new boolean[arr.length + 1];
		
		for(int i=0; i<arr.length; i++) {
			seen[arr[i]] = true;
		}
		
		for(int i=1; i<seen.length; i++) {
			if(!seen[i])
				return i;
		}
    
		return -1;
	}
}
