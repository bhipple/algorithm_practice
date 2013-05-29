/** 
 * Given a string, reverse its word order.
 * @author Ben
 *
 */

public class reverseString {

	public static void main(String[] args) {
		String y = "Hello, my name is Ben";
		System.out.println(y);
		y = reverseWordOrder(y);
		System.out.println(y);
	}
	
	public static String reverseWordOrder(String x) {
		x = reverse(x);
		String[] xParts = x.split(" ");
		StringBuffer buff = new StringBuffer();
		for(int i=0; i<xParts.length; i++) {
			xParts[i] = reverse(xParts[i]);
			buff.append(xParts[i] + " ");
		}
		buff.deleteCharAt(buff.length() - 1);
		return buff.toString();
	}
	
	public static String reverse(String x) {
		char[] str = x.toCharArray();
		
		int i = 0;
		int j = str.length - 1;
		
		while(i < j) {
			char t = str[i];
			str[i] = str[j];
			str[j] = t;
			i++;
			j--;
		}
		
		StringBuffer buff = new StringBuffer();
		
		for(int k=0; k<str.length; k++) {
			buff.append(str[k]);
		}
		return buff.toString();
	}
}
