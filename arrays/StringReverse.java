/**
 *  Reverse a string using a different data structure (chosen a stack here)
 */

import java.util.*;

public class StringReverse {

  /**
	 * @param args
	 */
	public static void main(String[] args) {
		String x = "Hello, world!";
		
		System.out.println(reverseString(x));
	}
	
	public static String reverseString(String s) {
		Stack<Character> st = new Stack<Character>();
		
		for(int i=0; i<s.length(); i++) {
			st.push(s.charAt(i));
		}
		
		StringBuffer buff = new StringBuffer();
		
		while(!st.isEmpty()) {
			buff.append(st.pop());
		}
		
		return buff.toString();
	}

}
