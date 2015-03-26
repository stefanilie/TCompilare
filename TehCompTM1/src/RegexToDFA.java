import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;


public class RegexToDFA {

	TreeBuilder tb;
	ArrayList<ArrayList<Integer>> followPos;
	DFA outputDFA;
	
	public DFA getOutputDFA() {
		return outputDFA;
	}

	public RegexToDFA() {
		tb = new TreeBuilder("NaN");
		
		String regex = "(abb|ba)*(a|b)*";
		//Node pizdaMasii = tb.parseAndBuild(regex);
		//System.out.println(pizdaMasii.getData());
		tb.depthFirstSearchAndBuildFunctions(tb.getRoot());
		System.out.println();
		this.followPos = tb.getFollowPos();
		
		
		State initSt  = new State(fromArrayToArrayList((tb.getRoot().getFirstPos())));
		outputDFA = new DFA(initSt);
		
		while(hasUnmarkedStates()) {
			ArrayList<State> auxStates = new ArrayList<State>(outputDFA.getStates());
			Iterator<State> it = auxStates.iterator();
			while(it.hasNext()){
				State st = it.next();
				if(!st.isMarked()) {
					st.setMarked(true);
					buildDFA(st);
				}
				
			}
		}	
	}
	
	public boolean hasUnmarkedStates() {
		Iterator<State> it = outputDFA.getStates().iterator();
		while(it.hasNext()) {
			State st = (State) it.next();
			if(!st.isMarked())
				//System.out.println
				return true;
		}
		return false;
			
	}
	
	
	
	public ArrayList<Integer> fromArrayToArrayList(int[] a) {
		ArrayList<Integer> aux = new ArrayList<Integer>();
		
		for(int i = 0; i < a.length; i++) {
			aux.add(a[i]);
		}
		
		return aux;
	}
	
	public void buildDFA(State st) {
		ArrayList<Integer> stateToCheck = new ArrayList<Integer>(st.getData());
		
		//char aux = tb.getIndexes()[stateToCheck.get(0)];
		//stateToCheck.remove(0);
		
		while(stateToCheck.size() > 0) {
			int initialIndex = stateToCheck.get(0);
			char transSymbol = tb.getIndexes()[initialIndex];
			ArrayList<Integer> path = new ArrayList<Integer>();
			
			
			path.addAll(followPos.get(initialIndex));
			HashSet<Integer> lol = new HashSet<Integer>(path);
			path = new ArrayList<Integer>(lol);
			stateToCheck.remove(0);
			
			if(transSymbol != '#') {
				for(int i = 0; i < stateToCheck.size(); i++) { //search for same letter index
					int currentIndex = stateToCheck.get(i);
					if(tb.getIndexes()[currentIndex] == transSymbol) {
						path.addAll(followPos.get(currentIndex));
						lol = new HashSet<Integer>(path);
						path = new ArrayList<Integer>(lol);
						stateToCheck.remove(i);
					}
				}
			
				State foundToState = new State(path);
				//ArrayList<Integer> test = new ArrayList<Integer>([1, 4, 6, 7, 8]);
				//System.out.println(new State())
				Transition foundTransition = new Transition(st, transSymbol, foundToState);
				if(!outputDFA.getStates().contains(foundToState))
					//System.out.println(outputDFA.getStates().contains(foundToState));
					outputDFA.addToStates(foundToState);
				if(!outputDFA.getTrans().contains(foundTransition))
					outputDFA.addToTrans(foundTransition);
			}	
		}
		
		//st.setMarked(true);
		//System.out.println(outputDFA.getStates());
		//sSystem.out.println(outputDFA.getTrans());
	}

	

	public static void main(String[] args) {
		
		RegexToDFA rtd = new RegexToDFA();
		System.out.println(rtd.getOutputDFA());
		
		//System.out.println(rtd.tb.getFollowPos());
		

	}

}
