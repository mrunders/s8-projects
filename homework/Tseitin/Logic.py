
from ConsList import *

class Boolean(object):

    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return "T" if self.value else "F"

    def value(self):
        return self.value

    def equal(self, bool):
        
        if type(bool) == Boolean:
            return self.value == bool.value()
        
        return False

    def negative(self):
        return BOT if self.value else TOP

TOP = Boolean(True)
BOT = Boolean(False)
NOT = "-"
AND = "*"
OR  = "+"
EQUIV = "="

class Unary(object):

    @staticmethod
    def negation(cons, only_current_cons=True):

        if not cons.is_empty():

            if only_current_cons:
                return ConsFactory.singleton(cons.car().negative())
            else:
                return cons.map(lambda x : x.negative())

        else:
            return cons