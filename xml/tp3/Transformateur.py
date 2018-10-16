
import xml.sax
import time
import cStringIO
import atexit

XML_SOURCE_FILE = "./dblp.xml"
RESULT_SET_FILE = "./resultSet.txt"
ELEMENT_DELIMITER = "|"
KEY_VALUE_DELIMITER = ":"

class ItemSet():

	def __init__(self):
		self.__data = [cStringIO.StringIO()]
		self.__pattern_in_last = False

	def append(self, key, value, pattern, index=-1):
		
		if (key[0] == 'a' and key[1] == 'u'):
			if value == pattern:
				self.__pattern_in_last = True
				
			self.__data[-1].write(key)
			self.__data[-1].write(KEY_VALUE_DELIMITER)
			self.__data[-1].write(value)
			self.__data[-1].write(ELEMENT_DELIMITER)
	
	def newLine(self):
		
		if self.__pattern_in_last:
			self.__data[-1].write("\n")
			self.__data.append(cStringIO.StringIO())
		else:
			self.__data[-1].close()
			self.__data[-1] = cStringIO.StringIO()

		self.__pattern_in_last = False
		self.__data[-1].seek(0)
		
	def getData(self):

		for i in self.__data:
			i.seek(0)

		return self.__data
		
	def freeData(self):
		for i in self.__data:
			i.close()


class TransformateurXML(xml.sax.ContentHandler):

	ITEMSET_NAME = ["article","inproceedings"]

	def __init__(self, pattern):

		self.__itemSet = []
		self.__balise_name = None
		self.__current_balise = None
		self.__parser = xml.sax.make_parser()
		self.__pattern = pattern

		for item in range(len(self.ITEMSET_NAME)):
			self.__itemSet.append(ItemSet())
	
	def startElement(self, name, attrs):

		try:
			self.__balise_name = self.ITEMSET_NAME.index(name)
			self.__itemSet[self.__balise_name].newLine()
		except ValueError:
			index_value = None

		self.__current_balise = name
		
	def endElement(self, name):
		
		if name in self.ITEMSET_NAME:
			self.__balise_name = None
	
	def characters(self, data):

		if (data != '\n') and (self.__balise_name != None):
			self.__itemSet[self.__balise_name].append(self.__current_balise.encode("utf-8"), data.encode("utf-8"), self.__pattern)
			
	def parse(self, file_dir=XML_SOURCE_FILE):
		
		ts = time.time()
		print("start parsing")
		self.__parser.setContentHandler(self)
		self.__parser.parse(file_dir)		
		ts = time.time() - ts
		print("Process executed in %f min" %  (ts / 60))
		return self.__itemSet

	def freeData(self):
		for i in self.__itemSet:
			i.freeData()

	def serialize(self):
		with open(RESULT_SET_FILE, "wt") as file:
			for item in self.__itemSet:
				data = item.getData()
				file.write("============================\n")
				for i in data:
					file.write(i.read())
					i.seek(0)



pattern="Fabien Delorme"
t = TransformateurXML(pattern=pattern)
atexit.register(t.freeData)
a = t.parse()
t.serialize()