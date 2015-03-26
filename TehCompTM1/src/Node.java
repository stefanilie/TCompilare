
public class Node {
	
	private char data;
	private Node left;
	private Node right;
	private boolean visited;
	private static int count = 0;
	private int index;
	private int[] firstPos;
	private int[] lastPos;
	private boolean isNullable;
	
	public Node(char data) {
		 this.firstPos = new int[10];
		 this.lastPos = new int[10];
		 this.setData(data);
		 this.setVisited(false);
	}

	public Node getLeftChild() {
		return left;
	}

	public void setLeftChild(Node left) {
		this.left = left;
	}

	public Node getRightChild() {
		return right;
	}

	public void setRightChild(Node right) {
		this.right = right;
	}

	public char getData() {
		return data;
	}

	public void setData(char data) {
		this.data = data;
	}

	public boolean isVisited() {
		return visited;
	}

	public void setVisited(boolean visited) {
		this.visited = visited;
	}

	public int getIndex() {
		return index;
	}

	public void setIndex(int index) {
		this.index = index;
	}

	public static int getCount() {
		return count;
	}

	public static void setCount(int count) {
		Node.count = count;
	}

	public int[] getFirstPos() {
		return firstPos;
	}

	public void setFirstPos(int[] firstPos) {
		this.firstPos = firstPos;
	}

	public int[] getLastPos() {
		return lastPos;
	}

	public void setLastPos(int[] lastPos) {
		this.lastPos = lastPos;
	}

	public boolean isNullable() {
		return isNullable;
	}

	public void setNullable(boolean isNullable) {
		this.isNullable = isNullable;
	}

	
}
