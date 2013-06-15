import java.util.*;

/**
 * Find the singleton in an integer array in which every other number appears exactly twice.
 * @author Ben
 *
 */
public class ArraySingleton {
	public static int findSingleton(int[] arr) {
		HashSet<Integer> hash = new HashSet<Integer>();
		
		for(int i=0; i<arr.length; i++) {
			if(!hash.add(arr[i]))
				hash.remove(arr[i]);
		}
		
		Iterator<Integer> iter = hash.iterator();
		
		return iter.next();	// If there is only 1 singleton, hash will have only one element.
	}

}
