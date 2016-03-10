import java.util.*;
/**
 * Find and return the common node of two linked lists merged into a ‘Y’ shape.
 * @author Ben
 *
 */
public class ListIntersection {
	
	public static ListNode findTheIntersection(ListNode A, ListNode B) {
		int lenA = 0;
		int lenB = 0;
		ListNode temp = A;
		while(temp != null) {
			lenA++;
			temp = temp.next;
		}
		temp = B;
		while(temp != null) {
			lenB++;
			temp = temp.next;
		}
		
		if(lenA > lenB) {
			for(int i=0; i<(lenA - lenB); i++) {
				A = A.next;
			}
		}
		if(lenB > lenA) {
			for(int i=0; i<(lenB - lenA); i++) {
				B = B.next;
			}
		}
		
		while(A != B && A != null && B != null) {
			A = A.next;
			B = B.next;
		}
		
		return A;
	}
}
