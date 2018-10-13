
import xml.sax

XML_SOURCE_FILE = "./low_dblp.xml"
RESULT_SET_FILE = "./resultSet.txt"
IGNORE_ATTRIBUTS = True
ELEMENT_DELIMITER = "|"
KEY_VALUE_DELIMITER = ":"

class ItemSet():

	def __init__(self, name):
		self.__data = []
		self.__header = []
		self.__selected = False
		self.__string_is_builded = False
	
	def isSelected(self):
		return self.__selected

	def select(self, state=True):
		self.__selected = state

	def append(self, key, data, index=-1):
		self.__data[index].append(key + KEY_VALUE_DELIMITER + data)

	def newLine(self, data):
		self.__data.append(data)

	def appendHeader(self, header):
		self.__header.append(header)

	def getData(self):

		if ( not self.__string_is_builded):
			self.__data = "\n".join([ELEMENT_DELIMITER.join(item) for item in self.__data])

		return self.__data

	def getHeader(self):
		return self.__header


class TransformateurXML(xml.sax.ContentHandler):

	ITEMSET_NAME = "article|inproceedings|proceedings|book|incollection|phdthesis|mastersthesis|www|person|data".split("|")

	IGNORE_ATTRIBUTS_FALSE = lambda v, attrs : ["-{}{}{}".format(attr, KEY_VALUE_DELIMITER, attrs[attr]) for attr in attrs.keys(), ELEMENT_DELIMITER]
	IGNORE_ATTRIBUTS_TRUE  = lambda v, x : []

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
			self.__itemSet[name].select()
			self.__itemSet[name].newLine( self.__initLine(attrs) )
			self.__balise_name = name

		self.__current_balise = name
		
	def endElement(self, name):

		if not self.__balise_name is None:
			self.__itemSet[self.__balise_name].select(state=False)
	
	def characters(self, data):

		if (not data == "\n"):
			self.__itemSet[self.__balise_name].append(self.__current_balise.encode("utf-8"), data.encode("utf-8"))
			
	def parse(self, file_dir=XML_SOURCE_FILE):

		self.__parser.setContentHandler(self)
		self.__parser.parse(file_dir)
		return self.__itemSet
		
	def save(self, dir_file=RESULT_SET_FILE):
		## only for visual.

		with open( dir_file, "wt" ) as file:
			for k,v in self.__itemSet.items():
				file.write(k)
				file.write("\n\n")
				file.write( v.getData())
				file.write("\n------------------------------------------------------\n")
	
t = TransformateurXML()
a = t.parse()
t.save()