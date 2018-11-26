package SaxGuy;

import java.io.FileWriter;
import java.io.IOException;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class ItemSetExtract extends ItemSetOutputFile {
	
	private String pattern;
	private String title, year;
	private StringBuilder fileout = new StringBuilder();
	private String attrKey;
	private Set<String> authorsList = new HashSet<String>();


	public ItemSetExtract(FileWriter output, String pattern) {
		super(output);
		this.pattern = pattern;
	}	
	
	
	@Override
	public void append(String key, String value) {
		if ( key == "author" ) {
			if (127 < value.charAt(0) && this.data.length() > 0 && value.charAt(0) != 201) {
				this.data.deleteCharAt(this.data.length()-1);
				this.data.deleteCharAt(this.data.length()-1);
			}
			
			this.data.append(value);
			this.data.append("&&");
		} else if (key == "title") {
			this.title = value;
		} else if (key == "year") {
			this.year = value;
		} else if (key == "key") {
			this.attrKey = value;
		}
		
	}

	public boolean newLine(String balise) {

		if (index++ != 0 && this.data.toString().contains(this.pattern)) {
			
			writeBalise("<", balise, " key='");
			writeBalise(this.attrKey, "'>", "");
				
			for (String s : this.data.toString().split("&&")) {
				if (s.length() > 0) {
					writeBalise("author", s);
					this.authorsList.add(s);
				}
			}
			writeBalise("title", this.title);
			writeBalise("year", this.year);
			writeBalise("</", balise, ">");
				
			this.fileout.append("\n");
		}

		this.data = new StringBuilder();
		return true;
	}
	
	private void writeBalise(String o, String key, String e) {
		
		this.fileout.append(o);
		this.fileout.append(key); 
		this.fileout.append(e);
	}
	
	private void writeBalise(String key, String value) {
		
		writeBalise("<", key, ">");
		this.fileout.append(value);
		writeBalise("</", key, ">");
	}
	
	public void append(String str) {
		try {
			this.output.write(str);
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	@Override
	public List<String> getData() {
		
		try {
			append("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n"
				 + "<!DOCTYPE dblp SYSTEM \"extract.dtd\">\n"
				 + "<?xml-stylesheet type=\"text/xsl\" href=\"xsltextract.xsl\" ?>"
				 + "\n<extract>\n");
			
			this.output.write("<name>"); this.output.write(this.pattern); this.output.write("</name>\n");
			this.output.write("<coauthors>");
			for (String s : this.authorsList) {
				this.output.write("<author>"); this.output.write(s); this.output.write("</author>");
			}
			this.output.write("</coauthors>\n");
			this.output.write(this.fileout.toString());
			append("</extract>");
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		return null;
	}

}
