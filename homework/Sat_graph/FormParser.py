
from ConsList import *

class Parser(object):

    def __init__(self, expr):

        self.expr = filter(lambda x : x != '', expr.replace("(", " ( ").replace(")", " ) ").replace("\\s", " ").strip().split(" "))
        self.profondeurReccurcive = 0
        self.indice = 0

    def value_format(self, expr):

        if expr == "TRUE" or expr == "true":
            return True
        elif expr == "FALSE" or expr == "false":
            return False

        return expr
    
    def __parse(self, expr):

        liste = ConsFactory.nil()

        if expr[self.indice] != '(':
            if len(expr) == 1:
                return self.value_format(expr[self.indice])
            
            else:
                raise "singleton de deux elements"

        self.indice += 1

        while ( self.indice < len(expr) ):

            if expr[self.indice] == '(':
                self.profondeurReccurcive += 1
                liste = liste.append(self.__parse(expr))
                self.profondeurReccurcive -= 1
            
            elif expr[self.indice] == ')':

                if self.profondeurReccurcive == 0 and self.indice + 1 < len(expr):
                    raise "chaine mal forme"

                return liste

            else:
                liste = liste.append(self.value_format(expr[self.indice]))

            self.indice += 1

        raise "pb de parentheses"

    def parse(self):
        return self.__parse(self.expr)
