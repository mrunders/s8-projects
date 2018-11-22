package SaxGuy;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

public class ItemSet {
	
	private String pattern;
	private int index = 0;
	private List<StringBuilder> data = new ArrayList<StringBuilder>();
	private boolean pattern_in_last = false;
	
	public ItemSet(String pattern) {
		this.pattern = pattern;
		this.data.add(new StringBuilder());
	}
	
	public void append(String key, String value) {
		if ( key == "author" ) {
			if ( this.pattern.equals(value) ) 
				this.pattern_in_last = true;
			
			this.data.get(this.index).append(value);
			this.data.get(this.index).append('|');
		}
	}
	
	public boolean newLine() {
		if (!this.pattern_in_last)
			this.data.remove(this.index);
		else this.index++;
		
		this.data.add(new StringBuilder());
		this.pattern_in_last = false;
		
		return true;
	}
	
	public List<StringBuilder> getData(){
		
		List<String> preResultSet = new ArrayList<String>();
		
		for (Iterator<StringBuilder> isb = this.data.iterator() ; isb.hasNext() ; ) {
			StringBuilder tmp = isb.next();
			if (!tmp.toString().contains(this.pattern)) isb.remove();
		}
		
		
		return this.data;
	}

}
