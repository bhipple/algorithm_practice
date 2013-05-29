/** 
 * Reverse a Linked List
 * @author Ben
 *
 */
public class LinkedListReverse {

  public static void main(String[] args) {
		ListNode a = new ListNode(5);
		a.next = new ListNode(6);
		a.next.next = new ListNode(7);
		a.next.next.next = new ListNode(8);
		
		System.out.println(reverse(a).next.next.next.data);
	}
	
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
