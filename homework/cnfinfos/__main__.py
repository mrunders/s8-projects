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
        return "%25s: %s" % (key, value)

    @staticmethod
    def __proportion(nb, total):
        return ((nb+0.0)/total)*100

    def __str__(self):
        nbcnf2 = len(list(filter(lambda x : len(x) == 2, self.cnf)))
        nbhorn = len(list(filter(lambda x : len(x) == 1, [list(filter(lambda x : x > 0, sl)) for sl in self.cnf])))
        nbreverse_horn = len(list(filter(lambda x : len(x) == 1, [list(filter(lambda x : x < 0, sl)) for sl in self.cnf])))
        l = len(self.cnf)

        name = self.__fstr("name", self.name)
        nb_vars = self.__fstr("nb variables", self.nb_vars)
        nb_lines = self.__fstr("nb lines", self.nb_lines)
        cnf = self.__fstr("ccnf", self.cnf)
        nb_2cnf = self.__fstr("nb 2cnf", nbcnf2)
        horn = self.__fstr("nb horn", nbhorn)
        horn_rev = self.__fstr("nb reverse horn", nbreverse_horn)
        proportion_2cnf = self.__fstr("proportion 2cnf", "%.2f" % (self.__proportion(nbcnf2, l)))
        proportion_horn = self.__fstr("proportion horn", "%.2f" % (self.__proportion(nbhorn, l)))
        proportion_reversehorn = self.__fstr("proportion reverse horn", "%.2f" % (self.__proportion(nbreverse_horn, l)))

        return "\n".join([name, nb_vars, nb_lines, nb_2cnf, horn, horn_rev, proportion_2cnf, proportion_horn, proportion_reversehorn, cnf])

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