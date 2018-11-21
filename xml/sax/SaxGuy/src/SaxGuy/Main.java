package SaxGuy;

import java.io.IOException;

import javax.xml.parsers.ParserConfigurationException;
import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

import org.xml.sax.SAXException;

public class Main {

	public static void main(String args[]) {
		
		
		try {
	        SAXParser parser = SAXParserFactory.newInstance().newSAXParser();
	        TransformateurHandle handler = new TransformateurHandle("Fabien Delorme");
	        parser.parse("dblp.xml", handler); 
		} catch (ParserConfigurationException e) {
			e.printStackTrace();
		} catch (SAXException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
}
