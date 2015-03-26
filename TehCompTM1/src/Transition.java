
public class Transition {

	private State fromState;
	private State toState;
	private char viaSymbol;
	
	public Transition(State fs, char vs, State ts) {
		this.fromState = fs;
		this.viaSymbol = vs;
		this. toState = ts;
	}
	
	@Override
	public String toString() {
		String aux = new String("");
		aux = "\n" + this.fromState.toString() + " -" + this.viaSymbol + "-> " + this.toState.toString();
		return aux;
	}

	public State getFromState() {
		return fromState;
	}

	public void setFromState(State fromState) {
		this.fromState = fromState;
	}

	public State getToState() {
		return toState;
	}

	public void setToState(State toState) {
		this.toState = toState;
	}

	public char getViaSymbol() {
		return viaSymbol;
	}

	public void setViaSymbol(char viaSymbol) {
		this.viaSymbol = viaSymbol;
	}

}
