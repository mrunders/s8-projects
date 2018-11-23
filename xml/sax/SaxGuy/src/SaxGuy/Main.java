package SaxGuy;

import java.io.FileWriter;

import javax.xml.parsers.SAXParser;
import javax.xml.parsers.SAXParserFactory;

public class Main {
	

	public static void main(String args[]) {
		
		if (args.length == 0) {
			System.out.println("Question 1:  ./dblp-prof-linux2 -name name dblp.xml");
			System.out.println("Question 2a: ./dblp-prof-linux2 -out file.gob dblp.xml");
			System.out.println("Question 2b: ./dblp-prof-linux2 -name name -in file.gob");
			System.out.println("Question 3:  ./dblp-prof-linux2 -name name dblp.xml -extract file.gob");
			System.out.println("Use *.gob or resultSet.txt as output file for gitignore");
		}
		
		if (args.length == 3) {
			
			if ("-name".equals(args[0])) {
				
				try {
			        SAXParser parser = SAXParserFactory.newInstance().newSAXParser();
			        parser.parse(args[2], new TransformateurHandle(args[1])); 
				} catch (Exception e) {
					e.printStackTrace();
				}
				
			} else if ( "-out".equals(args[0]) ){
				
				try {
			        SAXParser parser = SAXParserFactory.newInstance().newSAXParser();
			        parser.parse(args[2], new TransformateurHandle(new FileWriter(args[1]))); 
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		}
	
	}
}
