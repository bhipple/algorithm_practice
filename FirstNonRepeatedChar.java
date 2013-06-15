/**
 * Find the first non-repeated character in a string
 * @author Ben
 *
 */

public class FirstNonRepeatedChar {
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
}
