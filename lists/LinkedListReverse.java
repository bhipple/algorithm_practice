/** 
 * Reverse a Linked List
 * @author Ben
 *
 */
public class LinkedListReverse {
	public static ListNode reverse(ListNode a) {	
		ListNode b = a.next;
		a.next = null;
		
		while(b.next != null) {
			ListNode c = b.next;
			b.next = a;
			a = b;
			b = c;
		}
		b.next = a;
		return b;
	}
}
