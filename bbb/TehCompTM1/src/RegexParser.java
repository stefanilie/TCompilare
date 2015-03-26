
public class RegexParser {

	protected String input;
	protected int index;
	
	public RegexParser(String input) {
		this.setInput(input);
		this.index = input.length() - 1;
	}
	
	public boolean isTerm() {
		char c = input.charAt(index);
		if (c >= 97 && c <= 122)
			return true;
		else
			return false;
	}
	
	public boolean isTerm(char c) {
		if (c >= 97 && c <= 122)
			return true;
		else
			return false;
	}
	
	public boolean isKleene() {
		if(input.charAt(index) == '*')
			return true;
		else 
			return false;
	}
	
	public boolean isReunion() {
		if(input.charAt(index) == '|')
			return true;
		else 
			return false;
	}
	
	public char peek() {
		return input.charAt(index - 1);
	}
	
	public char lookAhead() {
		return input.charAt(index - 2);
	}
	
	public char eat() {
		index--;
		return input.charAt(index + 1);  //not sure
	}

	public void setIndex(int n) {
		this.index = n;
	}
	
	public void setInput(String input) {
		this.input = input;
	}
	
	

}
