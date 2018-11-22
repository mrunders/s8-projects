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
		this.data.add(new StringBuilder());
	}
	
	public void append(String key, String value) {
		if ( key == "author" ) {
			if ( this.pattern.equals(value) ) 
				this.pattern_in_last = true;
			
			this.data.get(this.index).append(value);
			this.data.get(this.index).append("&&");
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
	
	public List<String> getData(){
		
		List<StringBuilder> preResultSet = new ArrayList<StringBuilder>();
		
		for (StringBuilder strb : this.data) {
			String strs = strb.toString();
			if (strs.contains(this.pattern)) {
				for (String str : strs.split("&&")) {
					if ( !str.equals(this.pattern)) {
						if ( str.charAt(0) > 127 )
							preResultSet.get(preResultSet.size()-1).append(str);
						else 
							preResultSet.add(new StringBuilder(str));
					}
				}
			}
		}
		
		List<String> resultSet = new ArrayList<String>();
		for (StringBuilder ss : preResultSet)
			if (!resultSet.contains(ss.toString()))
				resultSet.add(ss.toString());
	
		return resultSet;
	}

}
