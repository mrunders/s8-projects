package SaxGuy;

import java.io.FileWriter;
import java.io.IOException;
import java.util.List;

public class ItemSetOutputFile implements IItemSet {
	
	protected int index = 0;
	protected FileWriter output;
	protected StringBuilder data = new StringBuilder();

	public ItemSetOutputFile(FileWriter output) {
		this.output = output;
	}

	@Override
	public void append(String key, String value) {
		if ( key == "author" ) {
			if (value.charAt(0) > 127 && this.data.length() > 0 && value.charAt(0) != 201) {
				this.data.deleteCharAt(this.data.length()-1);
				this.data.deleteCharAt(this.data.length()-1);
			}
			
			this.data.append(value);
			this.data.append("&&");
		}
		
	}

	@Override
	public boolean newLine() {
		if (index++ != 0 && this.data.length() > 0) {
			
			try {
				this.output.write(this.data.toString());
				this.output.write("\n");
				this.data = new StringBuilder();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		
		return true;
	}

	@Override
	public List<String> getData() {
		try {
			this.output.close();
		} catch (IOException e) {
			e.printStackTrace();
		}
		return null;
	}

}
