from Logic import Boolean,TOP,BOT,OR,AND
from ConsList import *

def remove_variables(cons):

    if type(cons) == Boolean:
        return cons

    if type(cons) == ConsList:
        return Solve.remove_vars(cons)

    if type(cons) == str:
        if cons[:4] == "var_":
            return TOP
        
        if cons[:5] == "-var_":
            return BOT

    return cons

def remove_terms(cons):

    if type(cons) == ConsList:

        cons = Solve.remove_terms(cons)

        if cons.car() == OR:
            if cons.contains(lambda x : x == TOP):
                return ""

            cons = cons.filter(lambda x : x != BOT)

        if cons.car() == AND:
            cons = cons.filter(lambda x : x != TOP)

        if cons.size() == 2:
            return cons.cdr().car()

    return cons


class Solve():

    @staticmethod
    def remove_vars(cons):
        return cons.map(remove_variables)
        
    @staticmethod
    def remove_terms(cons):
        return cons.map(remove_terms)