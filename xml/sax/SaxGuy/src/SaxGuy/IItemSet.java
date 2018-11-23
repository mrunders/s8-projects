package SaxGuy;

import java.util.List;

public interface IItemSet {
	
	public void append(String key, String value);
	public boolean newLine();
	public List<String> getData();
}
