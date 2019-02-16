import sys

variables = {}
model = ""

def split_color_name(var):

    name = ""

    v = 0
    while v < len(var) and not ('0' <= var[v] <= '9'):
        name += var[v]
        v += 1

    return name, var[v:]

## argv[1] = sat.out argv[2] = sat.in
with open(sys.argv[1]) as file:
    file.readline()
    model = [int(x) for x in file.readline().split(" ")[:-1]]

with open(sys.argv[2]) as file:
    values = file.readline()[:-1].split(" ")[1:]
    key = file.readline().split(" ")[1:]

for k,v in zip(key,values):
    variables[int(k)] = v

for m in model:
    if 0 < m:
        var = variables[m]
        print("%20s prendra la couleur %3s" % split_color_name(var) )
