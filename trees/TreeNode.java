import java.util.*;

public class TreeNode {

  private int data;
	private ArrayList<TreeNode> children;
	
	public TreeNode(int data) {
		this.data = data;
		children = new ArrayList<TreeNode>();
	}
	
	public void addChild(TreeNode n) {
		children.add(n);
	}
	
	public int numChildren() {
		return children.size();
	}
	
	public TreeNode getChild(int i) {
		return children.get(i);
	}
	
	public int getData() {
		return data;
	}
	
	public String toString() {
		return ""+data;
	}
}
