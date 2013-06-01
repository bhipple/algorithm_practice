import java.util.HashSet;

public class RemoveLinkedListDuplicates {
	
	public static void removeDuplicates(ListNode a) {
		if(a == null)
			return;
		
		HashSet<Integer> h = new HashSet<Integer>();
		h.add(a.data);
		
		while(a.next != null) {
			if(!h.add(a.next.data)) {
				a.next = a.next.next;
			}
			else 
				a = a.next;
		}
	}
}
