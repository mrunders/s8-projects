
#cnf dmax, minisat glucause

from functools import reduce
from ConsList import *
from FormParser import *

GRAPH_EXEMPLE_HEADER = ["wa","nt","sa","gld","nsw","vc","tas"]
GRAPH_EXEMPLE_DATA   = [("wa","nt"),("wa","sa"),("nt","sa"),("nt","gld"),("sa","gld"),("sa","nsw"),("sa","vc"),("gld","nsw"),("nsw","vc")]

AND_GATE = " . "
OR_GATE  = " + "
NOT_GATE = "-"
NEW_LINE = "\n"

class Sat_graph():

    def __init__(self, graph_variables, graph_data, nb_color=4):
        self.graph_variables = graph_variables
        self.graph_data = graph_data
        self.nb_color = nb_color

    def parse(self):
        return "(%s%s%s)" % (self.__sat_variables(), AND_GATE, self.__sat_constraints())

    def __sat_variables(self):
        return AND_GATE.join(map(lambda var : self.__sat_to_cnf_str(self.__variable_to_sat(var)), self.graph_variables))

    def __sat_constraints(self):
        return AND_GATE.join(self.__twos_vars_constraint_str())
    
    def __variable_to_sat(self, var):
        return map(lambda x : "%s%d" % (var, x) ,range(self.nb_color))

    def __sat_to_cnf_str(self, sat):
        return "(%s)" % (OR_GATE.join(sat))

    def __twos_vars_constraint_str(self):
        output = []
        for var1,var2 in self.graph_data:
            output.extend(self.__two_vars_constraint_str(var1,var2))
        return output

    def __two_vars_constraint_str(self, var1, var2):
        va1 = self.__variable_to_sat(var1)
        va2 = self.__variable_to_sat(var2)
        return map(lambda vv : "(%s%s%s(%s))" % (vv[0], OR_GATE, NOT_GATE, vv[1]), zip(va1,va2))

    def get_variables_names(self):
        return self.graph_variables

    def get_all_variables_names(self):
        output = []
        for var in self.graph_variables:
            output.extend(self.__variable_to_sat(var))
        return output

    @staticmethod
    def cnf_to_cons(cnf):
        return Parser(cnf).parse()

    @staticmethod
    def cons_to_dimacs(cons, variables_name):
        vars = { var : abs(hash(var)) for var in variables_name }
        new_cons = cons.map(lambda x : vars[x] if type(x) == str and len(x) > 1 else x)
        new_cons_str = "%s" % (new_cons.map(lambda x : NEW_LINE if x == "." else x))
        return new_cons_str.replace("(","").replace(")","").replace("%s " % (NOT_GATE), NOT_GATE)

    @staticmethod
    def write_dimacs_file(dimacs_str, variables_name, output_file=None):
        
        formated_dimacs = "p cnf %d %d\n%s" % (len(variables_name), dimacs_str.count(NEW_LINE), dimacs_str)
        
        if output_file is None:
            print(formated_dimacs)

        else:
            with open(output_file, "w") as file:
                file.write(formated_dimacs)
        
        


c = Sat_graph(nb_color=3, graph_variables=GRAPH_EXEMPLE_HEADER, graph_data=GRAPH_EXEMPLE_DATA)
d = Sat_graph.cnf_to_cons(cnf=c.parse())
e = Sat_graph.cons_to_dimacs(cons=d, variables_name=c.get_all_variables_names())
Sat_graph.write_dimacs_file(e, variables_name=c.get_all_variables_names())