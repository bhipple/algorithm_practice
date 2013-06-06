public class FindTreeHeight {
	
	public static int findDepth(TreeNode head) {
		if(head == null) {
			return 0;
		}
		
		int depth = 0;
		for(int i=0; i<head.numChildren(); i++) {
			depth = Math.max(depth, findDepth(head.getChild(i)));
		}
		
		return depth + 1;
	}
}
