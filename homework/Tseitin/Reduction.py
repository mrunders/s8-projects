from Logic import Boolean,TOP,BOT,OR,AND
from ConsList import *
from TseitinTransformation import VAR_SYMBOLE_PREFIX

def remove_variables(cons):

    if type(cons) == ConsList:
        cons =  Solve.simplity(cons)

        if cons.size() == 1 and cons.car() == TOP:
            return ""

        elif cons.car() == OR:
            if cons.contains(lambda x : x == TOP):
                return ""

            cons = cons.filter(lambda x : x != BOT)

        elif cons.car() == AND:
            if cons.contains(lambda x : x == BOT):
                return ""

            cons = cons.filter(lambda x : x != TOP)

        if cons.size() == 2: ## cons like "(OR x)" must be "x"
            return cons.cdr().car()

    elif type(cons) == str:
        if cons[:len(VAR_SYMBOLE_PREFIX)] == VAR_SYMBOLE_PREFIX:
            return TOP
        
        if cons[:1+len(VAR_SYMBOLE_PREFIX)] == "-" + VAR_SYMBOLE_PREFIX:
            return BOT

    return cons

class Solve():

    @staticmethod
    def simplity(cons):
        return cons.map(remove_variables).filter(lambda c : c != "")
