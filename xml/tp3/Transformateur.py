
import xml.sax
import cStringIO
import sys

ELEMENT_DELIMITER = "|"
KEY_VALUE_DELIMITER = ":"
END_OF_LINE = "\n"

class ItemSet():

	def __init__(self):
		self.__data = [""]
		self.__pattern_in_last = False

	def append(self, key, value, pattern, index=-1):
		if (key[0] == 'a' and key[1] == 'u'):
			if value == pattern:
				self.__pattern_in_last = True
				
			self.__data[-1] += value + ELEMENT_DELIMITER
	
	def newLine(self):
		if self.__pattern_in_last:
			self.__data[-1] += END_OF_LINE
			self.__data.append("")
		else:
			self.__data[-1] = ""

		self.__pattern_in_last = False
		
	def getData(self):
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
			self.__itemSet.append(self.__current_balise, data, self.__pattern)
			
	def parse(self, file_dir):
		self.__parser.setContentHandler(self)
		self.__parser.parse(file_dir)
		return self.__itemSet

	def freeData(self):
		self.__itemSet.freeData()

	def getResult(self):
		result = []
		x = []
		i = 0
		for items in self.__itemSet.getData():
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

                print("\n\n")
		print('"%s" has %d coauthors:' % (self.__pattern, len(x)))
		for i in x:
			print("-" + i)


t = TransformateurXML(pattern=sys.argv[1])
t.parse(file_dir=sys.argv[2])
t.getResult()
## t.freeData()

