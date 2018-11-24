package SaxGuy;

import java.io.FileWriter;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;

public class TransformateurHandlerExtracteur extends TransformateurHandle {
	
	private ItemSetExtract ise;

	public TransformateurHandlerExtracteur(FileWriter outputFile, String pattern) {
		super(pattern);	
		this.ise = new ItemSetExtract(outputFile, pattern);
	}
	
	public void startElement(String namespaceURI, String lname, String qName, Attributes attrs) throws SAXException {
		if (BALISES.contains(qName)) {
			this.balise_name = true;
			this.ise.newLine(qName);
			this.ise.append("key", attrs.getValue("key"));
		}
		
		this.current_balise = qName;
	}
	
	public void endElement(String uri, String localName, String qName) throws SAXException {
		if (BALISES.contains(qName)) 
			this.balise_name = false;
	}
	
	 public void characters(char[] data, int start, int end)  throws SAXException {
		 if (data[start] != '\n' && this.balise_name)
			 this.ise.append(this.current_balise, new String(data, start, end));
	 }
	 
	 public void endDocument() throws org.xml.sax.SAXException {
		 this.ise.getData();
	 }

}
