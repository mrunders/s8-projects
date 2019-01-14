from Case import *
from Solver import *

class Grille():

    solver_heuristique = SolverUtils.SOLVE

    def __init__(self, grid):

        self.grid = list()

        if type(grid[0]) == list:
            grid = [x for x in l for l in grid]

        self.grid = map(lambda x: Case(x), grid)
        
    def __str__(self):
        tmp = ""
        for i in range(9):
            for j in range(9):
                tmp += self.grid[i * 9 + j].__str__()
                tmp += " "
            tmp += "\n"
        return tmp

    def get(self, pos=None, posy=None):

        if posy != None:
            return self.grid[pos * 9 + posy]

        return self.grid if pos == None else self.grid[pos]

    def get_sequence(self, pos, instance_object=True):

        if type(pos) != list:
            return [self.get(pos)] if instance_object else [self.get(pos).get()]
        return [self.get(x) for x in pos] if instance_object else [self.get(x).get() for x in pos]

    def solve_find_cell_possible(self):

        if self.solver_heuristique == SolverUtils.SOLVE:
            solver = Solver()
            for posy in range(9):
                for posx in range(9):
                    if self.get(posx, posy).is_tmp() or self.get(posx, posy).is_none():
                        possible = solver.find_cell_possible(self, posx, posy)
                        self.get(posx, posy).notify(possible)

        elif self.solver_heuristique == SolverUtils.GRID_REDUCE:
            for posy in range(0,9,3):
                for posx in range(0,9,3):
                    Reducter.grid_elements(self, posx, posy)
        
        else:
            for pos in range(9):

                if self.solver_heuristique == SolverUtils.HORIZONTAL_REDUCE:
                    Reducter.horizontal_elements(self, pos)
                elif self.solver_heuristique == SolverUtils.vertical_elements:
                    Reducter.vertical_elements(self, pos)

        self.solver_heuristique = ( self.solver_heuristique + 1 ) % SolverUtils.SOLVER_SIZE

    def validation(self):
        return Validator.validation(grid=self)

    def getState(self):
        return SolverUtils.solver_state(self.solver_heuristique)