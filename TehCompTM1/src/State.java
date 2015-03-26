import java.util.ArrayList;


public class State {

	private ArrayList<Integer> data;
	private int index;
	static int count = 0;
	private boolean marked;
	
	public State(ArrayList<Integer> data) {
		this.setData(data);
		this.marked = false;
		count++;
		this.index = count;
	}
	
	@Override
	public String toString() {
		return data.toString();
	}
	
	@Override
	public boolean equals(Object obj) {
		if (obj == null) {
	        return false;
	    }
	    if (getClass() != obj.getClass()) {
	        return false;
	    }
	    final State other = (State) obj;
	    if((this.data == null) ? (other.data != null) : !this.data.equals(other.data))
	    	return false;
	    
	    return true;
	}

	public int getIndex() {
		return index;
	}

	public void setIndex(int index) {
		this.index = index;
	}

	public boolean isMarked() {
		return marked;
	}

	public void setMarked(boolean marked) {
		this.marked = marked;
	}

	public ArrayList<Integer> getData() {
		return data;
	}

	public void setData(ArrayList<Integer> data) {
		this.data = data;
	}

}
