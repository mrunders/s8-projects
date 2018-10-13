
import xml.sax
import Models

XML_SOURCE_FILE = "./low_dblp.xml"
RESULT_SET_FILE = "./resultSet.txt"
IGNORE_ATTRIBUTS = True
ELEMENT_DELIMITER = "|"
KEY_VALUE_DELIMITER = ":"

class ItemSet():

	def __init__(self, name):
		self.__data = None

	def append(self, key, data):

		if ( key in self.__data.keys()):
			self.__data[key] += self.__data[key] + ELEMENT_DELIMITER + data
		else:
			self.__data[key] = data

	def newLine(self, data):
		self.__data = data

	def pushOnDb(self):
		p = Models.Phdthesis.create(**self.__data)
		p.save()


class TransformateurXML(xml.sax.ContentHandler):

	ITEMSET_NAME = "article|inproceedings|proceedings|book|incollection|phdthesis|mastersthesis|www|person|data".split("|")

	IGNORE_ATTRIBUTS_FALSE = lambda v, attrs : dict((attr, attrs[attr]) for attr in attrs.keys())
	IGNORE_ATTRIBUTS_TRUE  = lambda v, x : {}

	def __init__(self):

		self.__itemSet = {}
		self.__balise_name = None
		self.__current_balise = None
		self.__parser = xml.sax.make_parser()

		self.__initLine = self.IGNORE_ATTRIBUTS_TRUE if IGNORE_ATTRIBUTS else self.IGNORE_ATTRIBUTS_FALSE

		for item in self.ITEMSET_NAME:
			self.__itemSet[item] = ItemSet(item)
	
	def startElement(self, name, attrs):

		if name in self.ITEMSET_NAME:
			self.__itemSet[name].newLine( self.__initLine(attrs) )
			self.__balise_name = name

		self.__current_balise = name
		
	def endElement(self, name):
		
		if name in self.ITEMSET_NAME:
			self.__itemSet[name].pushOnDb()
	
	def characters(self, data):

		if (not data == "\n"):
			self.__itemSet[self.__balise_name].append(self.__current_balise.encode("utf-8"),  data.encode("utf-8"))
			
	def parse(self, file_dir=XML_SOURCE_FILE):

		self.__parser.setContentHandler(self)
		self.__parser.parse(file_dir)
		return self.__itemSet


t = TransformateurXML()
a = t.parse()