
from ConsList import *
from Logic import AND,OR,NOT,TOP,BOT,EQUIV


class TseitinTransformation():

    def __init__(self):
        self.var_indice = 0
        self.operator = dict()

        self.operator[AND] = self.and_gate
        self.operator[OR]  = self.or_gate
        self.operator[EQUIV]=self.equiv_gate

    def __last_variable(self, negation=False):
        return "%svar_%d" % (NOT if negation else "" , self.var_indice)


    def __next_variable(self):
        self.var_indice += 1
        return self.__last_variable()

    def __negate(self, expr):
        if type(expr) == str:
            return expr[1:] if  expr[0] == "-" else "-%s" % (expr)

        elif type(expr) == ConsList:
            if expr.car() == NOT:
                return expr.cdr()
            else:
                return ConsFactory.singleton(NOT).append(expr)

        return expr

    def litteral(self, cons):

        if cons.size() != 1:
            raise "litteral must have size of 1"

        l_a = self.evaluate(cons.car())

        if l_a == TOP:
            new_var = self.__next_variable()
            return ConsFactory.as_list([AND, new_var, new_var])
            
        if l_a == BOT:
            new_var = self.__next_variable()
            return ConsFactory.as_list([AND, new_var, self.__negate(new_var)])

        return ConsFactory.as_list([AND, l_a, TOP])

    def and_gate(self, cons):

        if cons.car() != AND or cons.cdr().size() != 2:
            raise "AND binary operator only" + str(cons)

        new_var = self.__next_variable()
        neg_new_var = self.__negate(new_var)

        l_a = self.evaluate(cons.cdr().car())
        l_b = self.evaluate(cons.cdr().cdr().car())

        constmp4 = ConsFactory.as_list([OR,neg_new_var,l_b])
        constmp3 = ConsFactory.as_list([OR,neg_new_var,l_a])
        constmp2 = ConsFactory.as_list([OR, self.__negate(l_a), self.__negate(l_b), new_var])
        constmp1 = ConsFactory.singleton(new_var)
        return ConsFactory.as_list([AND, constmp1, constmp2, constmp3, constmp4])

    def or_gate(self, cons):

        if cons.car() != OR or cons.cdr().size() != 2:
            raise "OR binary operator only" + str(cons)

        new_var = self.__next_variable()
        neg_new_var = self.__negate(new_var)

        l_a = self.evaluate(cons.cdr().car())
        l_b = self.evaluate(cons.cdr().cdr().car())

        constmp4 = ConsFactory.as_list([OR,new_var,self.__negate(l_b)])
        constmp3 = ConsFactory.as_list([OR,new_var,self.__negate(l_a)])
        constmp2 = ConsFactory.as_list([OR, l_a, l_b, neg_new_var])
        constmp1 = ConsFactory.singleton(new_var)
        return ConsFactory.as_list([AND, constmp1, constmp2, constmp3, constmp4])

    def equiv_gate(self, cons):

        if cons.car() != EQUIV or cons.cdr().size() != 2:
            raise "OR binary operator only" + str(cons)

        new_var = self.__next_variable()
        neg_new_var = self.__negate(new_var)

        l_a = self.evaluate(cons.cdr().car())
        l_b = self.evaluate(cons.cdr().cdr().car())

        constmp5 = ConsFactory.as_list([OR,neg_new_var,self.__negate(l_a), l_b])
        constmp4 = ConsFactory.as_list([OR,neg_new_var,l_a, self.__negate(l_b)])
        constmp3 = ConsFactory.as_list([OR,new_var,l_a,l_b])
        constmp2 = ConsFactory.as_list([OR, new_var, self.__negate(l_a), self.__negate(l_b)])
        constmp1 = ConsFactory.singleton(new_var)
        return ConsFactory.as_list([AND, constmp1, constmp2, constmp3, constmp4, constmp5])

    def evaluate(self, cons):

        if type(cons) != ConsList:
            return cons

        car = cons.car()
        if car in self.operator.keys():
            return self.operator[car](cons)

        return self.litteral(cons)