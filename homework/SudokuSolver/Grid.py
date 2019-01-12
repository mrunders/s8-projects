from Case import *
from Solver import *

DEFAULT_GRID = [None,7,None,None,4,None,None,6,None,
                None,None,None,5,2,None,None,4,None,
                None,None,8,6,None,None,9,None,None,
                2,9,None,7,None,None,None,None,1,
                None,1,5,None,None,8,3,None,None,
                3,None,None,None,None,2,4,None,7,
                6,3,None,1,None,None,2,None,None,
                4,None,None,None,None,5,8,None,None,
                None,None,1,None,9,None,None,None,None]

class Grille():

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

        solver = Solver()
        for posy in range(9):
            for posx in range(9):
                if self.get(posx, posy).is_tmp() or self.get(posx, posy).is_none():
                    possible = solver.find_cell_possible(self, posx, posy)
                    self.get(posx, posy).notify(possible)

    def validation(self):
        return Validator.validation(grid=self)
                    