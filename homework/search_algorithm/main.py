
import os

from sklearn.preprocessing import normalize

FILE_PATH = "data-00007-of-00010.gob"
SHORTER_FILE = "shorter.gob"

if not os.path.exists(SHORTER_FILE):
	print("generating %s file" % (SHORTER_FILE))
	## reduce data by ignore useless lines
	output = open(SHORTER_FILE, "w")
	with open(FILE_PATH, "r") as inpu:
	    for line in inpu:
	        if line[0] == 'U':
	            output.write(line)
	        elif line[0] == '\n':
	            output.write("\n")
	        elif line[0] == 'M':
	            items = line.split("\t")
	            output.write(items[3])
	        
	output.close()
	print("done")


print("size reduction")
data = dict()

with open(SHORTER_FILE, "r") as inpu:
    for line in inpu:
        if line[0] == 'U':
            url = line.split("\t")[1][:-1]
        elif line[0] != "\n":
            line = line[:-1]
            try:
                data[line] += 1
            except:
                data[line] = 1

print("done")

data_header = data.keys()
data_values = data.values()
data.clear()

data_values_normalized = normalize(data_values, norm=’l2’, axis=1, copy=True, return_norm=False)