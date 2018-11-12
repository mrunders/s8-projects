package SaxGuy;

import java.util.ArrayList;
import java.util.List;

public class ItemSet {
	
	private String pattern;
	private int index = 0;
	private List<StringBuilder> data = new ArrayList<StringBuilder>();
	private boolean pattern_in_last = false;
	
	public ItemSet(String pattern) {
		this.pattern = pattern;
	}
	
	public void append(String key, String value) {
		if ( key.charAt(0) == 'a' && key.charAt(1) == 'u' ) {
			if ( value == this.pattern ) this.pattern_in_last = true;
			this.data.get(this.index).append(value);
			this.data.get(this.index).append('|');
		}
	}
	
	public void newLine() {
		if (this.pattern_in_last) {
			this.data.get(this.index++).append('\n');
			this.data.add(new StringBuilder());
		} else {
			this.data.get(this.index).setLength(0);
		}
		
		this.pattern_in_last = false;
	}
	
	public List<StringBuilder> getData(){
		return this.data;
	}

}
