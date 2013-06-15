package amazon;
import java.util.*;
/**
 * Find the first non-repeated character in a string.
 * 
 * Solution to two different versions of the problem given (second one is the harder version)
 * 
 * @author Ben
 *
 */

public class FirstNonRepeatedChar {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		String str = "abfbfbbcdgda";
		
		System.out.println(firstUnique(str));
	}
	
	// Assuming by "repeated" we mean two of them adjacent to each other
	// Runtime: O(n)
	// Additional Space: O(1)
	public static char firstNonRepeated(String str) {
		if(str.charAt(0) != str.charAt(1))
			return str.charAt(0);
		
		for(int i=1; i<str.length() - 1; i++) {
			if(str.charAt(i) != str.charAt(i+1)) {
				if(str.charAt(i) != str.charAt(i-1)) {
					return str.charAt(i);
				}
			}
			else
				i++;
		}
		
		if(str.charAt(str.length() - 1) != str.charAt(str.length() - 2))
				return str.charAt(str.length() - 1);
		return '-';
	}
	
	// Without the above assumption (i.e., by 'non-repeated' we mean 'unique')
	// Runtime: O(n)
	// Additional Space: O(n)
	public static char firstUnique(String str) {
		Hashtable<Character, Integer> ht = new Hashtable<Character, Integer>();
		
		for(int i=0; i<str.length(); i++) {
			if(!ht.containsKey(str.charAt(i))) {
				ht.put(str.charAt(i),  i);
			}
			else if(ht.get(str.charAt(i)) != -1) {
				ht.remove(str.charAt(i));
				ht.put(str.charAt(i),  -1);
			}
		}
		
		Enumeration<Character> e = ht.keys();
		while(e.hasMoreElements()) {
			char key = e.nextElement();
			if(ht.get(key) == -1)
				ht.remove(key);
		}
		
		Enumeration<Integer> f = ht.elements();
		int first = Integer.MAX_VALUE;
		while(f.hasMoreElements()) {
			int val = f.nextElement();
			if(val < first)
				first = val;
		}
		
		if(first < str.length()) 
			return str.charAt(first);
		else
			return '-';
	}
}
