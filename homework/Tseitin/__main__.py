
from ConsList import *
from Logic import *
from FormParser import Parser
from TseitinTransformation import *
from Reduction import *

def evaluate(expr):
    return TseitinTransformation().evaluate(Parser(expr).parse())

"""
print(evaluate("(-p)"))
print(evaluate("(TRUE)"))
print(evaluate("(FALSE)"))
print(evaluate("(* p q)"))
print(evaluate("(+ p q) "))
print(evaluate("(+ p -q)"))
print(evaluate("(* ( + p q ) ( + -p -q))"))
"""

expr = evaluate("(= p (* p r))")
print(expr)
sol = Solve.remove_vars(expr)
print(sol)
cc = Solve.remove_terms(sol)
print(cc)