/**
 * Given a tree(not a binary tree) and 2 TreeNodes on the tree. 
 * Give an algorithm to find the least common ancestor of the given TreeNodes. 
 * @author Ben
 *
 */

  import java.util.*;

public class TreeLeastCommonAncestor {

	Stack<TreeNode> sa;
	Stack<TreeNode> sb;
	
	
	public TreeLeastCommonAncestor() {

	}
	
	public TreeNode lcAncestor(TreeNode a, TreeNode b, TreeNode head) {
		sa = new Stack<TreeNode>();
		sb = new Stack<TreeNode>();
		
		dfs(head, a, sa);
		dfs(head, b, sb);
		
		TreeNode res = head;
		while(!sa.isEmpty() && !sb.isEmpty()) {
			if(sa.peek() == sb.peek()) {
				res = sa.pop();
				sb.pop();
			}
			else {
				sa.pop();
				sb.pop();
			}
		}
		
		return res;
	}
	
	
	private boolean dfs(TreeNode head, TreeNode target, Stack<TreeNode> sr) {
		if(head == target) {
			sr.add(head);
			return true;
		}

		boolean foundTar = false;
		for(int i=0; i<head.numChildren(); i++) {
			if(dfs(head.getChild(i), target, sr)) {
				sr.add(head);
				foundTar = true;
				i = head.numChildren();
			}
		}
		return foundTar;
	}
}
