import java.util.*;

/**
 * Given a value val and coin denominations coins[], return the minimum number of coins to necessary to make val dollars
 * @author Ben
 *
 */
public class MinCoins {	
	public static int findMinCoins(int[] coins, int val) {
		Arrays.sort(coins);
		int[] best = new int[val+1];
		Arrays.fill(best, Integer.MAX_VALUE);
		
		for(int i=0; i<coins.length; i++) {
			if(coins[i] <= val)
				best[coins[i]] = 1;
			else
				return best[val];
			for(int j=1; j<best.length; j++) {
				if(best[j] != Integer.MAX_VALUE && (j + coins[i] < best.length)) {
					if(best[j+coins[i]] > best[j] + 1)
						best[j+coins[i]] = best[j] + 1;
				}
			}
		}
		return best[val];
	}

}
