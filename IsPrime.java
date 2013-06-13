import java.util.*;

/**
**  Determine if a number N is prime.
**/

public class IsPrime {

	public static boolean isPrime(int n) {
		int lim = (int) Math.sqrt(n);
		if(n == 2)
			return true;
		
		for(int i=2; i<=lim; i++) {
			if(n%i == 0)
				return false;
		}
		return true;
	}
}
