  /** 
  * Given a tree, output a linked list of all nodes in the tree ordered by level.
  **/
  
  public class TreeToBreadthList {
    public static LinkedList treeToBreadthList(TreeNode head) {
  
  		LinkedList<Integer> res = new LinkedList<Integer>();
  		
  		LinkedList<TreeNode> q = new LinkedList<TreeNode>();
  		q.add(head);
  		
  		while(!q.isEmpty()) {
  			TreeNode t = q.removeFirst();
  			res.add(t.data);
  			
  			for(int i=0; i<t.numChildren(); i++) {
  				q.add(t.getChild(i));
  			}
  		}
  		return res;
  	}
  }
