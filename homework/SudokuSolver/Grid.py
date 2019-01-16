from Case import *
from Solver import *

class Grille():

    solver_heuristique = 0
    blocked = 0
    
    MIN_FOR_BLOCKED = SolverUtils.SOLVER_SIZE + 2
    prediction_solve = list()

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

    def get(self, pos=None, posy=None, instance_object=True):

        if pos == None:
            return self.grid
        elif posy != None:
            cell = self.grid[pos * 9 + posy]
            return cell if instance_object else cell.get()
        elif type(pos) == list:
            grid = [self.get(x) for x in pos]
            return grid if instance_object else map(lambda x : x.get(), grid)
        else:
            cell = self.grid[pos]
            return cell if instance_object else cell.get()

        return None

    def solve_find_cell_possible(self):

        if self.blocked == self.MIN_FOR_BLOCKED:
            self.prediction_solve.append(Prediction(self.grid, self.getFirstTuple()))
            self.prediction_solvation()
            
        else:
            solved_something = False
            solver_state = SolverUtils.solver_state(self.solver_heuristique)
            if solver_state == SolverUtils.SOLVE:
                for posy in range(9):
                    for posx in range(9):
                        if self.get(posx, posy).is_tmp() or self.get(posx, posy).is_none():
                            possible = Solver.find_cell_possible(self, posx, posy)
                            self.get(posx, posy).notify(possible)

            elif solver_state == SolverUtils.GRID_REDUCE:
                for posy in range(0,9,3):
                    for posx in range(0,9,3):
                        solved_something = Reducter.grid_elements(self, posx, posy)
            
            else:
                for pos in range(9):
                    if solver_state == SolverUtils.HORIZONTAL_REDUCE:
                        solved_something = Reducter.horizontal_elements(self, pos)
                    elif solver_state == SolverUtils.VERTICAL_REDUCE:
                        solved_something = Reducter.vertical_elements(self, pos)

            self.solver_heuristique = ( self.solver_heuristique + 1 ) % SolverUtils.SOLVER_SIZE
            self.blocked = self.blocked + 1 if not solved_something else 0

            if not self.is_solvable():
                if len(self.prediction_solve) > 0:
                    self.swap_grid(self.prediction_solve[-1].get_backup())
                    self.prediction_solvation()
        
    def prediction_solvation(self):
        if not self.prediction_solve[-1].next_prediction_test():
            self.swap_grid(self.prediction_solve.pop(-1).get_backup())
        self.blocked = 0

    def validation(self):
        return len( filter(lambda x : x.is_constante(), self.grid) ) == len(self.grid) and  Validator.validation(grid=self)

    def getState(self):
        return SolverUtils.solver_state(self.solver_heuristique)

    def getFirstTuple(self):
        for cell in self.grid:
            if len(cell.get_all()) == 2:
                return cell

    def is_solvable(self):
        return len(filter(lambda x : x.is_none(), self.grid)) == 0

    def swap_grid(self, new_grid):
        if new_grid != None:
            for i in range(len(new_grid)):
                self.grid[i].notify(new_grid[i].get_all())
            