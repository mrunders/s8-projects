
from Grid import *
from Case import *

class SolverUtils():

    SOLVE = 0
    HORIZONTAL_REDUCE = 1
    VERTICAL_REDUCE = 2
    GRID_REDUCE = 3
    SOLVER_SIZE = 4

    SOLVER_STATES = ["Solve", "Horizontal reduce", "Vertical reduce", "Grid reduce"]

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
            tmp = grid.get_sequence(map(lambda x: x + 3 *multiplier, [0,1,2,9,10,11,18,19,20]))
        elif ind_grid_x < 6:
            tmp = grid.get_sequence(map(lambda x: x + 3 *multiplier, [27,28,29,36,37,38,45,46,47]))
        else:
            tmp = grid.get_sequence(map(lambda x: x + 3 * multiplier, [54,55,56,63,64,65,72,73,74]))

        return tmp

    @staticmethod
    def horizontal_elements(grid, ind_grid_y):
        return grid.get_sequence(map(lambda x: x + 9 * ind_grid_y, range(9)))

    @staticmethod
    def vertical_elements(grid, ind_grid_x):
        return grid.get_sequence(map(lambda x: x + ind_grid_x, [0,9,18,27,36,45,54,63,72]))

class Solver():

    def __init__(self):
        pass

    def get_vertical_line(self, grid, posx, posy):
        tmp = list()
        for i in range(9):
            if i != posy:
                cell = grid.get(posx, i)
                if cell.is_constante():
                    tmp.append(cell.get())

        return tmp

    def get_horizontal_line(self, grid, posx, posy):
        tmp = list()
        for i in range(9):
            if i != posx:
                cell = grid.get(i, posy)
                if cell.is_constante():
                    tmp.append(cell.get())  
        
        return tmp

    def get_grid_line(self, grid, posx, posy):
        return map(lambda x: x.get(), filter(lambda x: x.is_constante(), SolverUtils.get_grid_elements(grid, posx, posy)))

    def find_cell_possible(self, grid, posx, posy):
        cell = grid.get(posx, posy)

        notPossibletmp = self.get_vertical_line(grid, posx, posy)
        notPossibletmp.extend(self.get_horizontal_line(grid, posx, posy))
        notPossibletmp.extend(self.get_grid_line(grid, posx, posy))
        notPossible = set(notPossibletmp)

        return filter(lambda x: not x in notPossible , range(1,10))

class Reducter():

    @staticmethod
    def reduct(picked_elements):

        elements = filter(lambda x: x.is_tmp(), picked_elements)

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
                    if len(values) == 1:
                        key.notify(values)

    @staticmethod
    def grid_elements(grid, ind_grid_x, ind_grid_y):
        Reducter.reduct(SolverUtils.get_grid_elements(grid, ind_grid_x, ind_grid_y))

    @staticmethod
    def horizontal_elements(grid, ind_grid_y):
        Reducter.reduct(SolverUtils.horizontal_elements(grid, ind_grid_y))

    @staticmethod
    def vertical_elements(grid, ind_grid_x):
        Reducter.reduct(SolverUtils.vertical_elements(grid, ind_grid_x))  


class Validator():

    @staticmethod
    def same_list(sequence):
        return sorted([x.get_all() for x in sequence]) == range(1,10)

    @staticmethod
    def horizontal_validation(grid):
        sequence = range(9)
        for i in range(9):
            if Validator.same_list(grid.get_sequence(sequence)):
                return False

            sequence = map(lambda x : x + 9, sequence)

        return True

    @staticmethod
    def vertical_validation(grid):
        sequence = [0,9,17,27,36,45,54,63,72]
        for i in range(9):
            if Validator.same_list(grid.get_sequence(sequence)):
                return False

            sequence = map(lambda x : x + 1, sequence)

        return True

    @staticmethod
    def grid_validation(grid):
        NORMAL_SET = range(1,10)
        return Validator.same_list(grid.get_sequence([0,1,2,9,10,11,18,19,20])) and\
               Validator.same_list(grid.get_sequence([3,4,5,12,13,14,21,22,23])) and\
               Validator.same_list(grid.get_sequence([6,7,8,15,16,17,24,25,26])) and\
               Validator.same_list(grid.get_sequence([27,28,29,36,37,38,45,46,47])) and\
               Validator.same_list(grid.get_sequence([30,31,32,39,40,41,48,49,50])) and\
               Validator.same_list(grid.get_sequence([33,34,35,42,43,44,51,52,53])) and\
               Validator.same_list(grid.get_sequence([54,55,56,63,64,65,72,73,74])) and\
               Validator.same_list(grid.get_sequence([57,58,59,66,67,68,75,76,77])) and\
               Validator.same_list(grid.get_sequence([60,61,62,69,70,71,78,79,80]))

    @staticmethod
    def validation(grid):
        return Validator.horizontal_validation(grid) and Validator.vertical_validation(grid) and Validator.grid_validation(grid)
               