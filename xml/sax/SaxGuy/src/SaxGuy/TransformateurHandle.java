package SaxGuy;

import java.util.ArrayList;
import java.util.List;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

public class TransformateurHandle extends DefaultHandler {
	
	private static List<String> ITEMSET_NAME = new ArrayList<>();
	private ItemSet itemSet;
	private String current_balise;
	
	@SuppressWarnings("unused")
	private String pattern;
	
	private boolean balise_name = false;

	public TransformateurHandle(String pattern) {
		this.itemSet = new ItemSet(pattern);
		this.pattern = pattern;
		
		ITEMSET_NAME.add("article");
		ITEMSET_NAME.add("inproceedings");
	}
	
	public void startElement(String namespaceURI, String lname, String qName, Attributes attrs) throws SAXException {
		
		this.balise_name = ITEMSET_NAME.contains(qName);
		if ( this.balise_name ) this.itemSet.newLine();
		this.current_balise = qName;
		
	}
	
	public void endElement(String uri, String localName, String qName) throws SAXException {
		if ( ITEMSET_NAME.contains(qName) ) {
			this.balise_name = false;
		}
	}
	
	 public void characters(char[] data, int start, int end)  throws SAXException {
		 if (data[start] != '\n' && this.balise_name)
			 this.itemSet.append(this.current_balise, new String(data, start, end));
	 }
	 
	  public void endDocument() throws SAXException {
		  this.itemSet.getData().forEach(System.out::println);
	  }
}
