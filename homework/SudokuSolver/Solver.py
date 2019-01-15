
from Grid import *
from Case import *

class SolverUtils():

    SOLVE = "Solve"
    HORIZONTAL_REDUCE = "Horizontal reduce"
    VERTICAL_REDUCE = "Vertical reduce"
    GRID_REDUCE = "Grid reduce"

    SOLVER_STATES = [SOLVE, HORIZONTAL_REDUCE, SOLVE, VERTICAL_REDUCE, SOLVE, GRID_REDUCE]
    SOLVER_SIZE = len(SOLVER_STATES)

    @staticmethod
    def solver_state(state):
        return SolverUtils.SOLVER_STATES[state]

    @staticmethod
    def unpack_list_of_list(array):
        return [item for sublist in array for item in sublist]

    @staticmethod
    def get_grid_elements(grid, ind_grid_x, ind_grid_y):

        multiplier = 0 if ind_grid_y < 3 else 1 if ind_grid_y < 6 else 2

        if ind_grid_x < 3:
            tmp = grid.get(map(lambda x: x + 3 *multiplier, [0,1,2,9,10,11,18,19,20]))
        elif ind_grid_x < 6:
            tmp = grid.get(map(lambda x: x + 3 *multiplier, [27,28,29,36,37,38,45,46,47]))
        else:
            tmp = grid.get(map(lambda x: x + 3 * multiplier, [54,55,56,63,64,65,72,73,74]))

        return tmp

    @staticmethod
    def horizontal_elements(grid, ind_grid_y):
        return grid.get(map(lambda x: x + 9 * ind_grid_y, range(9)))

    @staticmethod
    def vertical_elements(grid, ind_grid_x):
        return grid.get(map(lambda x: x + ind_grid_x, [0,9,18,27,36,45,54,63,72]))

class Solver():

    @staticmethod
    def get_vertical_line(grid, posx, posy):
        tmp = list()
        for i in range(9):
            if i != posy:
                cell = grid.get(posx, i)
                if cell.is_constante():
                    tmp.append(cell.get())

        return tmp

    @staticmethod
    def get_horizontal_line(grid, posx, posy):
        tmp = list()
        for i in range(9):
            if i != posx:
                cell = grid.get(i, posy)
                if cell.is_constante():
                    tmp.append(cell.get())  
        
        return tmp

    @staticmethod
    def get_grid_line(grid, posx, posy):
        return map(lambda x: x.get(), filter(lambda x: x.is_constante(), SolverUtils.get_grid_elements(grid, posx, posy)))

    @staticmethod
    def find_cell_possible(grid, posx, posy):
        cell = grid.get(posx, posy)

        notPossibletmp = Solver.get_vertical_line(grid, posx, posy)
        notPossibletmp.extend(Solver.get_horizontal_line(grid, posx, posy))
        notPossibletmp.extend(Solver.get_grid_line(grid, posx, posy))
        notPossible = set(notPossibletmp)

        return filter(lambda x: not x in notPossible , range(1,10))

class Reducter():

    @staticmethod
    def reduct(elements):

        solved_something = False
        if len(elements) > 1:
            elts = map(lambda x: x.get_all(), elements)
            all_elts = SolverUtils.unpack_list_of_list(elts)

            tmp_dict = dict()
            for e in set(all_elts):
                if all_elts.count(e) == 1:
                    tmp = filter(lambda elt : e in elt.get_all(), elements)
                    if len(tmp) == 1:
                        if tmp[0] in tmp_dict:
                            tmp_dict[tmp[0]].append(e)
                        else :
                            tmp_dict[tmp[0]] = [e]
            
            if len(tmp_dict) > 0:
                for key, values in tmp_dict.items():
                    if len(values) == 1 and key.get_all() != values:
                        key.notify(values)
                        solved_something = True
        
        return solved_something

    @staticmethod
    def grid_elements(grid, ind_grid_x, ind_grid_y):
        return Reducter.reduct(SolverUtils.get_grid_elements(grid, ind_grid_x, ind_grid_y))

    @staticmethod
    def horizontal_elements(grid, ind_grid_y):
        return Reducter.reduct(SolverUtils.horizontal_elements(grid, ind_grid_y))

    @staticmethod
    def vertical_elements(grid, ind_grid_x):
        return Reducter.reduct(SolverUtils.vertical_elements(grid, ind_grid_x))  

class Validator():

    NORMAL_RANGE = range(1,10)

    @staticmethod
    def same_list(sequence):
        return sorted([x.get() for x in sequence]) == Validator.NORMAL_RANGE

    @staticmethod
    def horizontal_validation(grid):
        sequence = range(9)
        for i in range(9):
            if Validator.same_list(grid.get(sequence)):
                return False

            sequence = map(lambda x : x + 9, sequence)

        return True

    @staticmethod
    def vertical_validation(grid):
        sequence = [0,9,17,27,36,45,54,63,72]
        for i in range(9):
            if Validator.same_list(grid.get(sequence)):
                return False

            sequence = map(lambda x : x + 1, sequence)

        return True

    @staticmethod
    def grid_validation(grid):            
        
        for posy in range(0,9,3):
            for posx in range(0,9,3):
                if not Validator.same_list(SolverUtils.get_grid_elements(grid, posx, posy)):
                    return False

        return True

    @staticmethod
    def validation(grid):
        return Validator.horizontal_validation(grid) and Validator.vertical_validation(grid) and Validator.grid_validation(grid)
               
