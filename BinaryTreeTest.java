// Check to see if a binary tree is a binary search tree.

public class BinaryTreeTest {
	
	public static boolean isBinaryTree(BinaryTreeNode head) {
		return isBinaryTree(head, Integer.MIN_VALUE, Integer.MAX_VALUE);
	}
	
	private static boolean isBinaryTree(BinaryTreeNode head, int min, int max) {
		if(head == null)
			return true;
		if(head.data < min || head.data > max)
			return false;
		
		return (isBinaryTree(head.left, min, head.data - 1) && isBinaryTree(head.right, head.data + 1, max));
	}
}
