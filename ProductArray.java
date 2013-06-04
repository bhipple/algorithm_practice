import java.util.*;
/**
 * Given array of numbers [S1, S2, ...Sn], calculate the result array R whose Ri=S1*..S[i-1]*S[i+1]*…*Sn. Require 2 solutions.
 * @author Ben
 *
 */
public class ProductArray {

	// O(n) solution
	public static int[] prodArray(int[] s) {
		int zeroLoc = -1;
		int product = 1;
		int[] res = new int[s.length];
		
		for(int i=0; i<s.length; i++) {
			if(s[i] == 0) {
				// Two zeros
				if(zeroLoc != -1) {
					Arrays.fill(res, 0);
					return res;
				} else {
					zeroLoc = i;
				}
			} else
				product = product * s[i];
		}
		
		// One zero
		if(zeroLoc != -1) {
			Arrays.fill(res, 0);
			res[zeroLoc] = product;
		} else {
			for(int i=0; i<res.length; i++) {
				res[i] = product / s[i];
			}
		}
		return res;
	}
	
	// O(n^2) solution
	public static int[] productArray(int[] s) {
		int[] res = new int[s.length];
		Arrays.fill(res, 1);
		
		for(int i=0; i<res.length; i++) {
			for(int j=0; j<s.length; j++) {
				if(i != j)
					res[i] = res[i] * s[j];
			}
		}
		return res;
	}
}
