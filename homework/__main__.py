from __future__ import division

import sys

class Cnf():

    def __init__(self, name=None, nb_vars=None, nb_lines=None, cnf=list()):
        self.name = name
        self.nb_vars = nb_vars
        self.nb_lines = nb_lines
        self.cnf = cnf

    @staticmethod
    def __fstr(key,value):
        return "%20s: %s" % (key, value)

    def __str__(self):
        cnf2 = len(list(filter(lambda x : len(x) == 2, self.cnf)))

        name = self.__fstr("name", self.name)
        nb_vars = self.__fstr("nb variables", self.nb_vars)
        nb_lines = self.__fstr("nb lines", self.nb_lines)
        cnf = self.__fstr("ccnf", self.cnf)
        nb_2cnf = self.__fstr("nb 2cnf", cnf2)
        proportion_2cnf = self.__fstr("proportion 2cnf", "%.3f" % (cnf2+0.0/len(self.cnf)) )
        horn = self.__fstr("nb horn", len(list(filter(lambda x : len(x) == 1, [list(filter(lambda x : x > 0, sl)) for sl in self.cnf]))))
        horn_rev = self.__fstr("nb horn reverse", len(list(filter(lambda x : len(x) == 1, [list(filter(lambda x : x < 0, sl)) for sl in self.cnf]))))

        return "\n".join([name, nb_vars, nb_lines, nb_2cnf, proportion_2cnf, horn, horn_rev, cnf])

class DmacsReader():

    @staticmethod
    def parse(path):

        cnfc = Cnf(name=path.split("/")[-1])
        with open(path, 'r') as file:
            for line in file:
                if line[0] == 'c':
                    pass
                elif line[0] == 'p':
                    tmp = line.split(" ")
                    cnfc.nb_lines = int(tmp.pop(-1))
                    cnfc.nb_vars  = int(tmp.pop(-1))
                else:
                    cnfc.cnf.append([int(x) for x in line.split(" ")[:-1]])

        return cnfc



file = sys.argv[1] if len(sys.argv) == 2 else sys.stdin
print(DmacsReader.parse(file))