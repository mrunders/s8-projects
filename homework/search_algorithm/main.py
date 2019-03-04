
import os
import numpy
from copy import deepcopy
from itertools import repeat
from sklearn.preprocessing import normalize

FILE_PATH = "data-00007-of-00010_shorter.gob"
SHORTER_FILE = "data_shorter.gob"
WORDS_KEYS = "words_link.gob"
LINKS_LIST = "link_list.gob"

links = list()

if not os.path.exists(LINKS_LIST):
	## reduce data by ignore useless lines
	if not os.path.exists(SHORTER_FILE):
		print("generating %s file" % (SHORTER_FILE))
		output = open(SHORTER_FILE, "w")
		with open(FILE_PATH, "r") as inpu:
			for line in inpu:
				if line[0] == 'U':
					output.write(line)
					links.append(line[4:])
				elif line[0] == '\n':
					output.write("\n")
				elif line[0] == 'M':
					items = line.split("\t")
					output.write("LINK ")
					output.write(items[1])
					output.write(" ")
					output.write(items[3])
				
		output.close()
		print("done")

	with open(LINKS_LIST, "w") as output:
		print("saving all links")
		for l in links:
			output.write(l)
		print("done")

else:
	with open(LINKS_LIST, "r") as inpu:
		print("getting all links")
		for l in inpu:
			links.append(l)
		print("done")

print(len(links))
len_matrix = len(links)
matrix = numpy.zeros((len_matrix,len_matrix), dtype='?')

for i in range(len_matrix):
	matrix[i][i] = 1

print(matrix)