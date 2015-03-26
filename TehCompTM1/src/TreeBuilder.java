import java.util.ArrayList;


public class TreeBuilder extends RegexParser {

	private Node root;
	private Node currentNode;
	private ArrayList<ArrayList<Integer>> followPos;
	private char[] indexes;
	
	public TreeBuilder(String input) {
		super(input);
		root = new Node('.');
		String regex = "(abb|ba)*(a|b)*";
		root.setRightChild(new Node('#'));
		followPos = new ArrayList<ArrayList<Integer>>(11);
		root.setLeftChild(parseAndBuild(regex));
		
		//justBuild();
		
		//. . * | . . a b b . b a * | a b # 
		for(int i = 1; i < 11; i++) 
			followPos.add(new ArrayList<Integer>());
		
		indexes = new char[10];
	}
	
	public Node getRoot() {
		return this.root;
	}
	
	public char[] getIndexes() {
		return this.indexes;
	}
	
	public Node concatTerm() {
		Node n = new Node('.');
		n.setRightChild(new Node(eat()));
		currentNode.setLeftChild(n);
		currentNode = n;
		return n;
	}
	
	public Node concatKleeneTree() {
		Node n = new Node('.');
		Node k = new Node(eat());
		k.setLeftChild(new Node(eat()));
		n.setRightChild(k);
		currentNode.setLeftChild(n);
		currentNode = n;
		return n;
	}

	/*
	public Node parseAndBuild(String regex) {
		index = regex.length() - 1;
		Node n;
		while(index >= 0) {
			int rIndex = 0;//scanForReunion(regex);
			if(rIndex > 0) {
				n = new Node('|');
				n.setLeftChild(parseAndBuild(regex.substring(0, rIndex - 1)));
				n.setRightChild(parseAndBuild(regex.substring(rIndex + 1, regex.length())));
				return n;
			} else {
				n = new Node('.');
				n.setRightChild(new Node(regex.charAt(index)));
				index--;
				while(index >= 0) {
					if(index > 1) { //aa*b
						Node aux =  new Node('.');
						if(regex.charAt(index) != '*') {
							aux.setRightChild(new Node(regex.charAt(index)));
							index--;
						} else {
							Node n2 = new Node('*');
							n2.setLeftChild(new Node(regex.charAt(index - 1)));
							if(index - 1 > 0) { //aa*
								aux.setRightChild(n2);
							} else if (index - 1 == 0) //a*
								aux.setLeftChild(n2);
						}
					}
				}
			}
		}
			
	}
	*/
	
	public int scanForReunion(String regex) {
		int i = regex.length() - 1;
		//System.out.println(regex);
		while(i >= 1)
			if(regex.charAt(i) == ')')
				i = scanForNextLParen(regex.substring(0, i));
			else if(regex.charAt(i) == '|')
				return i;
			else i--;
		return -1;
	}
	
	public Node reunionTree(String lRegex, String rRegex) {
		Node aux = new Node('|');
		aux.setRightChild(parseAndBuild(rRegex));
		aux.setLeftChild(parseAndBuild(lRegex));
		return aux;
	}
	
	public int scanForNextLParen(String regex) {
		for(int i = regex.length() - 1; i >= 0; i--) {
			if(regex.charAt(i) == '(')
				return i;
		}
		return -1;
	}
	
	public class Auxclass {
		
		private int idx;
		private Node nodeData;
		
		public Auxclass(int returnIdx, Node nodeData) {
			this.idx =returnIdx;
			this.nodeData = nodeData;
		}
		
		public int getIdx() {
			return idx;
		}

		public Node getNodeData() {
			return nodeData;
		}

		
		
	}
	
	public Auxclass parseAndBuildOnce(String regex) {
		int currentInput = regex.length() - 1;
			//System.out.println(regex.charAt(currentInput));
		if(currentInput > -1) {
			int rIdx =  scanForReunion(regex);
			System.out.println(rIdx);
			if(rIdx > 0) {
				//System.out.println(regex.substring(0, rIdx));
				Node nodeData = reunionTree(regex.substring(0, rIdx), regex.substring(rIdx + 1 , currentInput));
				Auxclass data = new Auxclass(0, nodeData);
				return data;
			} else if(regex.charAt(currentInput) == ')') {
				int lParenIdx = scanForNextLParen(regex.substring(0, currentInput));
				Node nodeData = parseAndBuild(regex.substring(lParenIdx + 1, currentInput));
				Auxclass data = new Auxclass(lParenIdx, nodeData);
				return data;
			} 
			else if(isTerm(regex.charAt(currentInput))) {
				Node currentNode = new Node('.');
				currentNode.setLeftChild(new Node(regex.charAt(currentInput)));
				Auxclass data = new Auxclass(currentInput - 1, currentNode);
				return data;
			}
		}
			return null;
	}
	
	public Node parseAndBuild(String regex) {
		
		int currentInput = regex.length() - 1;
		if(currentInput > -1);
				//System.out.println(regex.charAt(currentInput));
		
		//System.out.println(rIdx);
		if(currentInput > -1) {
			int rIdx =  scanForReunion(regex);
			if(rIdx > 0) {
				Node x = reunionTree(regex.substring(0, rIdx), regex.substring(rIdx + 1, currentInput + 1));
				//System.out.println(x.getData());
				return x;
			} else if(regex.charAt(currentInput) == ')') {
				int lParenIdx = scanForNextLParen(regex.substring(0, currentInput));
				Node x = parseAndBuild(regex.substring(lParenIdx + 1, currentInput));
				//System.out.println(x.getData());
				return x;
			} else if(isTerm(regex.charAt(currentInput))) {
				if(currentInput > 0 && currentInput - 1 != ('(')) {
					Node currentNode = new Node('.');
					currentNode.setRightChild(new Node(regex.charAt(currentInput)));
					currentNode.setLeftChild(parseAndBuild(regex.substring(0,currentInput)));
					return currentNode;
				} else if(currentInput == 0 || currentInput - 1 == ('(')) {
					Node currentNode = new Node(regex.charAt(currentInput));
					return currentNode;
				}
			} else if(regex.charAt(currentInput) == '*') {
				Auxclass idxAndNode = parseAndBuildOnce(regex.substring(0,currentInput));
				if(idxAndNode.getIdx() > 0) {
					Node currentNode = new Node('.');
					currentNode.setRightChild(new Node('*'));
					Node kleeneSide = currentNode.getRightChild();
					kleeneSide.setLeftChild(idxAndNode.getNodeData());
					currentNode.setLeftChild(parseAndBuild(regex.substring(0, idxAndNode.getIdx())));
					return currentNode;
				} else {
					Node currentNode = new Node('*');
					currentNode.setLeftChild(idxAndNode.getNodeData());
					return currentNode;
				}
			}
		}
		return null;
	}
	
	
	public void justBuild() {
		root.setLeftChild(new Node('.'));
		Node n = root.getLeftChild();
		n.setLeftChild(new Node('*'));
		n.setRightChild(new Node('*'));
		Node n2 = n.getRightChild();
		n2.setLeftChild(new Node('|'));
		n2 = n2.getLeftChild();
		n2.setLeftChild(new Node('a'));
		n2.setRightChild(new Node('b'));
		n = n.getLeftChild();
		n.setLeftChild(new Node('|'));
		n = n.getLeftChild();
		n.setLeftChild(new Node('.'));
		n.setRightChild(new Node('.'));
		n2 = n.getRightChild();
		n2.setLeftChild(new Node('b'));
		n2.setRightChild(new Node('a'));
		n = n.getLeftChild();
		n.setRightChild(new Node('b'));
		n.setLeftChild(new Node('.'));
		n = n.getLeftChild();
		n.setLeftChild(new Node('a'));
		n.setRightChild(new Node('b'));
		
	}
	
	public ArrayList<ArrayList<Integer>> getFollowPos() {
		return this.followPos;
	}
	
	public int[] concatArrays(int[] a, int[] b) {
		int[] aux = new int[a.length + b.length];
		
		System.arraycopy(a, 0, aux, 0, a.length);
		System.arraycopy(b, 0, aux, a.length, b.length);
		
		return aux;
		
	}
	
	public void depthFirstSearchAndBuildFunctions(Node n) {
		n.setVisited(true);
		System.out.print(n.getData() + " " );
		
		
		if(n.getLeftChild() != null && !n.getLeftChild().isVisited())
			depthFirstSearchAndBuildFunctions(n.getLeftChild());
		if(n.getRightChild() != null && !n.getRightChild().isVisited())
			depthFirstSearchAndBuildFunctions(n.getRightChild());
		if(isTerm(n.getData()) || n.getData() == '#') {
			Node.setCount(Node.getCount() + 1);
			n.setIndex(Node.getCount());
			indexes[Node.getCount()] = n.getData();
			int[] aux = new int[1];
			aux[0] = Node.getCount();
			n.setFirstPos(aux);
			n.setLastPos(aux);
			n.setNullable(false);
		} else
		if(n.getData() == '.' && (n.getRightChild() != null && n.getLeftChild() != null)) {
			n.setNullable(n.getLeftChild().isNullable() && n.getRightChild().isNullable());
			if(n.getLeftChild().isNullable())
				n.setFirstPos(concatArrays(n.getLeftChild().getFirstPos(), n.getRightChild().getFirstPos()));
			else
				n.setFirstPos(n.getLeftChild().getFirstPos());
			
			if(n.getRightChild() != null && n.getRightChild().isNullable())
				n.setLastPos(concatArrays(n.getRightChild().getLastPos(), n.getLeftChild().getLastPos()));
			else
				n.setLastPos(n.getRightChild().getLastPos());
			
			int[] lp = n.getLeftChild().getLastPos();
			int[] fp = n.getRightChild().getFirstPos();
			
			for (int i = 0; i < lp.length; i++)
				for(int j = 0; j < fp.length; j++)
					followPos.get(lp[i]).add(fp[j]);	
		} else if(n.getData() == '|' && (n.getRightChild() != null && n.getLeftChild() != null)) {
			n.setNullable(n.getLeftChild().isNullable() || n.getRightChild().isNullable());
			n.setFirstPos(concatArrays(n.getLeftChild().getFirstPos(), n.getRightChild().getFirstPos()));
			n.setLastPos(concatArrays(n.getLeftChild().getLastPos(), n.getRightChild().getLastPos()));
		} else if(n.getData() == '*') {
			n.setNullable(true);
			n.setFirstPos(n.getLeftChild().getFirstPos());
			n.setLastPos(n.getLeftChild().getLastPos());
			
			int[] lp = n.getLeftChild().getLastPos();
			int[] fp = n.getLeftChild().getFirstPos();
			
			for (int i = 0; i < lp.length; i++)
				for(int j = 0; j < fp.length; j++)
					followPos.get(lp[i]).add(fp[j]);
		} 
	}
	
}
