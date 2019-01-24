
from ConsList import *
from Logic import *
from FormParser import Parser
from TseitinTransformation import *
from Reduction import *

def tseitin(expr):
    return TseitinTransformation().evaluate(Parser(expr).parse())

def extseitin(expr):
    print("Pour %s" % (str(expr)))
    print(">> %s" % (tseitin(expr)))


extseitin("(-p)")
extseitin("(TRUE)")
extseitin("(FALSE)")
extseitin("(* p r)")
extseitin("(+ p r) ")
extseitin("(+ p -r)")
extseitin("(* ( + p r ) ( + -p -r))")
extseitin("(= p (* p r))")
extseitin("(= p (* p r))")
