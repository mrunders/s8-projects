package SaxGuy;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

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

}
