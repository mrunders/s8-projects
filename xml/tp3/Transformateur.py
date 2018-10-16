
import xml.sax

XML_SOURCE_FILE = "./dblp.xml"
RESULT_SET_FILE = "./resultSet.txt"
ELEMENT_DELIMITER = "|"
KEY_VALUE_DELIMITER = ":"

class ItemSet():

	def __init__(self):
		self.__data = []

	def append(self, key, value, index=-1):
		self.__data[index] += key + KEY_VALUE_DELIMITER + value + ELEMENT_DELIMITER
	
	def newLine(self):
		self.__data.append("")


class TransformateurXML(xml.sax.ContentHandler):

	ITEMSET_NAME = ["article","inproceedings"]

	def __init__(self, pattern=""):

		self.__itemSet = {}
		self.__balise_name = None
		self.__current_balise = None
		self.__parser = xml.sax.make_parser()
		self.__pattern = "author" + KEY_VALUE_DELIMITER + pattern

		for item in self.ITEMSET_NAME:
			self.__itemSet[item] = ItemSet()
	
	def startElement(self, name, attrs):

		if name in self.ITEMSET_NAME:
			self.__itemSet[name].newLine()
			self.__balise_name = name

		self.__current_balise = name
		
	def endElement(self, name):
		pass
	
	def characters(self, data):

		if (not data[0] == '\\' and not self.__balise_name is None):
			self.__itemSet[self.__balise_name].append(self.__current_balise.encode("utf-8"), data.encode("utf-8"))
			
	def parse(self, file_dir=XML_SOURCE_FILE):
		
		print("starting parsing")
		self.__parser.setContentHandler(self)
		self.__parser.parse(file_dir)
		return self.__itemSet
	
t = TransformateurXML(pattern="Carmen Heine")
a = t.parse()
