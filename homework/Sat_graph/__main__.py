from itertools import combinations
import sys
import json

NOT_GATE = "-"

class jsonParser():

    def __init__(self, path="tmp.json"):
        self.data = ""
        with open(path, "r") as file:
            self.data = json.load(file)

        self.variables = self.data["variables"]
        self.constraints = self.data["constraints"]

    def get_variables(self):
        return self.variables 

    def get_constraints(self):
        return self.constraints

class Sat_graph():

    def __init__(self, graph_variables, graph_data, nb_color=4):
        self.graph_variables = graph_variables
        self.graph_data = graph_data
        self.nb_color = nb_color

    def parse(self):
        variables = []
        constraintes = []

        for var in self.graph_variables:
            tmp = Sat_graph.all_clause_for_one_variable(var, self.nb_color)
            variables.append(tmp[0])

            for a in tmp[1]:
                constraintes.append(a)

        for constr1, constr2 in self.graph_data:
            constr1 = Sat_graph.all_vars_for_one_var(constr1, self.nb_color)
            constr2 = Sat_graph.all_vars_for_one_var(constr2, self.nb_color)
            for const in zip(constr1,constr2):
                constraintes.append(list(const))

        variables_name = self.get_all_variables_names()
        vars = { var : variables_name.index(var)+1 for var in variables_name }

        variables = list(map(lambda x : ["%s" % (vars[y]) for y in x], variables))
        constraintes = list(map(lambda x : list(map(lambda y : "%s%s" % (NOT_GATE, vars[y]), x)), constraintes))

        return variables, constraintes, len(vars)

    @staticmethod
    def all_clause_for_one_variable(var, nb_colors):
        a = Sat_graph.all_vars_for_one_var(var, nb_colors)
        return a, Sat_graph.vars_combinations(a)

    @staticmethod
    def all_vars_for_one_var(var, nb_colors):
        return ["%s%d" % (var, x) for x in range(nb_colors)]

    @staticmethod
    def vars_combinations(vars, arite=2):
        return [[x[0],x[1]] for x in combinations(vars, arite)]

    def get_all_variables_names(self):
        output = []
        for var in self.graph_variables:
            output.extend(Sat_graph.all_vars_for_one_var(var, self.nb_color))
        return output

    @staticmethod
    def write_dimacs_file(real_variable_names, variables, constraintes, nb_variables, output_file=None):
        
        dimacs_str = ""

        comm = " ".join(real_variable_names)

        for vars in variables:
            dimacs_str += "%s 0\n" % (" ".join(vars))

        comm += "\nc " + dimacs_str[:].replace("0\n","")

        for const in constraintes:
            dimacs_str += "%s 0\n" % (" ".join(const))

        formated_dimacs = "c %s\np cnf %d %d\n%s" % (comm,nb_variables, len(variables) + len(constraintes), dimacs_str)
        
        if output_file is None or output_file.lower() == "none":
            print(formated_dimacs)

        else:
            with open(output_file, "w") as file:
                file.write(formated_dimacs)
        
        

if __name__ == "__main__":
    data = jsonParser(path=sys.argv[1])
    variables, constraints = data.get_variables(), data.get_constraints()
    sat = Sat_graph(nb_color=int(sys.argv[2]), graph_variables=variables, graph_data=constraints)

    variables, constraints, nb_variables = sat.parse()
    output_file = None if len(sys.argv) == 3 else sys.argv[3]
    real_variable_names = sat.get_all_variables_names()

    Sat_graph.write_dimacs_file(real_variable_names, variables,constraints,nb_variables, output_file=output_file)