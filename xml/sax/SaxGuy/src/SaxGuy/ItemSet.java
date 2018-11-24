package SaxGuy;

import java.util.ArrayList;
import java.util.List;

public class ItemSet implements IItemSet {
	
	protected String pattern;
	protected int index = 0;
	protected List<StringBuilder> data = new ArrayList<StringBuilder>();
	
	public ItemSet(String pattern) {
		this.pattern = pattern;
		this.data.add(new StringBuilder());
	}
	
	public void append(String key, String value) {
		if ( key == "author" ) {
			if (value.charAt(0) > 127 && this.data.get(this.index).length() > 0) {
				this.data.get(this.index).deleteCharAt(this.data.get(this.index).length()-1);
				this.data.get(this.index).deleteCharAt(this.data.get(this.index).length()-1);
			}
			
			this.data.get(this.index).append(value);
			this.data.get(this.index).append("&&");
		}
	}
	
	public boolean newLine() {
		if (!this.data.get(this.index).toString().contains(this.pattern)) 
			this.data.remove(this.index);
		else 
			this.index++;
		
		this.data.add(new StringBuilder());
		return true;
	}
	
	public List<String> getData(){
		
		List<StringBuilder> preResultSet = new ArrayList<StringBuilder>();
		
		for (StringBuilder strb : this.data) {
			String strs = strb.toString();
			if (strs.contains(this.pattern)) {
				for (String str : strs.split("&&")) {
					if ( !str.equals(this.pattern)) {
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
