/** 
* Print the contents of a binary search tree in in-order, pre-order, and post-order traversals
**/

public class BSTprint {
  public static void inOrder(BinaryTreeNode head) {		
		if(head == null)
			return;
		inOrder(head.left);
		res += head.data + ", ";
		inOrder(head.right);
	}
	
	public static void preOrder(BinaryTreeNode head) {
		if(head == null)
			return;
		res += head.data + ", ";
		preOrder(head.left);
		preOrder(head.right);
	}
	
	public static void postOrder(BinaryTreeNode head) {
		if(head == null)
			return;
		postOrder(head.left);
		postOrder(head.right);
		res += head.data + ", ";
	}
	
	public static String res = "";
}
