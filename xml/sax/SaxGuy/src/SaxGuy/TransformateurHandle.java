package SaxGuy;

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
	
	private ItemSet itemSet;
	private String current_balise;
	private String pattern;
	
	private boolean balise_name = false;

	public TransformateurHandle(String pattern) {
		this.itemSet = new ItemSet(pattern);
		this.pattern = pattern;
	
	}
	
	public void startElement(String namespaceURI, String lname, String qName, Attributes attrs) throws SAXException {
		this.balise_name = BALISES.contains(qName) && this.itemSet.newLine();
		this.current_balise = qName;
	}
	
	public void endElement(String uri, String localName, String qName) throws SAXException {
		this.balise_name = BALISES.contains(qName);
	}
	
	 public void characters(char[] data, int start, int end)  throws SAXException {
		 if (data[start] != '\n' && this.balise_name)
			 this.itemSet.append(this.current_balise, new String(data, start, end));
	 }
	 
	  public void endDocument() throws SAXException {
		  System.out.println(this.pattern + " has " + this.itemSet.getData().size() + " coauthors:");
		  for (StringBuilder s : this.itemSet.getData()) {
			  System.out.println("- " + s);
		  }
	  }
}
