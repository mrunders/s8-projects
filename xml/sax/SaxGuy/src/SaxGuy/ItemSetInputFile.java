package SaxGuy;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class ItemSetInputFile extends ItemSet {
	
	private BufferedReader inputFile;

	public ItemSetInputFile(FileReader inputFile, String pattern) {
		super(pattern);
		
		this.inputFile = new BufferedReader(inputFile);
		
		try {
			process();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
	}
	
	private void process() throws IOException {
		
		String line;
		for ( ; ((line=this.inputFile.readLine()) != null) && line.length() > 0 ; ) {
			if ( line.contains(this.pattern))
				super.data.add(new StringBuilder(line));
		}
		
	}
	
	@Override
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
