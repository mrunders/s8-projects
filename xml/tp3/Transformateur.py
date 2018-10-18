
import xml.sax
import time
import cStringIO

SHOW_TIMER = False

XML_SOURCE_FILE = "./dblp.xml"
RESULT_SET_FILE = "./resultSet.txt"
ELEMENT_DELIMITER = "|"
KEY_VALUE_DELIMITER = ":"
END_OF_LINE = "\n"

class ItemSet():

	def __init__(self):
		self.__data = [cStringIO.StringIO()]
		self.__pattern_in_last = False

	def append(self, key, value, pattern, index=-1):
		if (key[0] == 'a' and key[1] == 'u'):
			if value == pattern:
				self.__pattern_in_last = True
				
			self.__data[-1].write(value)
			self.__data[-1].write(ELEMENT_DELIMITER)
	
	def newLine(self):
		if self.__pattern_in_last:
			self.__data[-1].write(END_OF_LINE)
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
		self.__itemSet = ItemSet()
		self.__balise_name = None
		self.__current_balise = None
		self.__parser = xml.sax.make_parser()
		self.__pattern = pattern
	
	def startElement(self, name, attrs):
		try:
			self.__balise_name = self.ITEMSET_NAME.index(name)
			self.__itemSet.newLine()
		except ValueError:
			index_value = None

		self.__current_balise = name
		
	def endElement(self, name):
		if name in self.ITEMSET_NAME:
			self.__balise_name = None
	
	def characters(self, data):
		if (data != END_OF_LINE) and (self.__balise_name != None):
			self.__itemSet.append(self.__current_balise, data.encode("utf-8"), self.__pattern)
			
	def parse(self, file_dir=XML_SOURCE_FILE):
		if SHOW_TIMER:
			ts = time.time()
			print("start parsing")

		self.__parser.setContentHandler(self)
		self.__parser.parse(file_dir)

		if SHOW_TIMER:
			ts = time.time() - ts
			print("Process executed in %f min" %  (ts / 60))

		return self.__itemSet

	def freeData(self):
		self.__itemSet.freeData()

	def getResult(self):
		result = []
		x = []
		i = 0
		for line in self.__itemSet.getData():
			items = line.read()
			if self.__pattern in items:
				for item in items.split(ELEMENT_DELIMITER):
					if item != self.__pattern and item != END_OF_LINE:
						result.append(item)

		while i < len(result):
			x.append(result[i])
			i += 1
			while i < len(result) and not result[i][0].isupper():
				x[-1] += result[i]
				i += 1
			if x.index(x[-1]) < len(x)-1:
				x.pop()

		print('"%s" has %d coauthors:' % (self.__pattern, len(x)))
		for i in x:
			print(i)


pattern="Fabien Delorme"
t = TransformateurXML(pattern=pattern)
t.parse()
t.getResult()
t.freeData()

