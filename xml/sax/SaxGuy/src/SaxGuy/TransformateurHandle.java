package SaxGuy;

import java.io.FileReader;
import java.io.FileWriter;
import java.util.ArrayList;
import java.util.List;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

public class TransformateurHandle extends DefaultHandler {
	
	public static List<String> BALISES = new ArrayList<>();
	
	static {
		BALISES.add("article");
		BALISES.add("inproceedings");
	}
	
	protected IItemSet itemSet;
	protected String current_balise;
	protected String pattern = null;
	
	protected boolean balise_name = false;

	public TransformateurHandle(String pattern) {
		this.itemSet = new ItemSet(pattern);
		this.pattern = pattern;
	
	}
	
	public TransformateurHandle(FileWriter output) {
		this.itemSet = new ItemSetOutputFile(output);
	}
	
	public TransformateurHandle(FileReader inputFile, String pattern) {
		this.itemSet = new ItemSetInputFile(inputFile, pattern);
		this.pattern = pattern;
	}

	public void startElement(String namespaceURI, String lname, String qName, Attributes attrs) throws SAXException {
		if (BALISES.contains(qName)) {
			this.balise_name = true;
			this.itemSet.newLine();
		}
		
		this.current_balise = qName;
	}
	
	public void endElement(String uri, String localName, String qName) throws SAXException {
		if (BALISES.contains(qName)) 
			this.balise_name = false;
	}
	
	 public void characters(char[] data, int start, int end)  throws SAXException {
		 if (data[start] != '\n' && this.balise_name)
			 this.itemSet.append(this.current_balise, new String(data, start, end));
	 }
	 
	  public void printResult() {
		  List<String> l = this.itemSet.getData();
		  if ( l != null ) {
			  System.out.println(this.pattern + " has " + l.size() + " coauthors:");
			  for (String s :l) {
				  System.out.println("- " + s);
			  }
		  }
	  }
}
