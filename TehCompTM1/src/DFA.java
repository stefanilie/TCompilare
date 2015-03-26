import java.util.ArrayList;


public class DFA {

	private ArrayList<State> states;
	private ArrayList<Transition> trans;
	private State initialState;
	
	public DFA(State st) {
		this.setInitialState(st);
		this.states = new ArrayList<State>();
		this.trans = new ArrayList<Transition>();
		this.states.add(st);
	}
	


	public ArrayList<Transition> getTrans() {
		return trans;
	}

	public void addToTrans(Transition ts) {
		this.trans.add(ts);
	}

	public State getInitialState() {
		return initialState;
	}

	public void setInitialState(State initialState) {
		this.initialState = initialState;
	}

	public ArrayList<State> getStates() {
		return states;
	}

	public void addToStates(State st) {
		states.add(st);
	}
	
	@Override
	public String toString() {
		String aux = new String("");
		
		aux = aux + this.getStates() + "\n" + this.getTrans();
		
		return aux;
	}
}
