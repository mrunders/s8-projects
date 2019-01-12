
from Grid import *
from Case import *

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
        tmp = list()
        multiplier = 0 if posy < 3 else 1 if posy < 6 else 2

        if posx < 3:
            tmp = grid.get_sequence(map(lambda x: x + 3 *multiplier, [0,1,2,9,10,11,18,19,20]))
        elif posx < 6:
            tmp = grid.get_sequence(map(lambda x: x + 3 *multiplier, [27,28,29,36,37,38,45,46,47]))
        else:
            tmp = grid.get_sequence(map(lambda x: x + 3 * multiplier, [54,55,56,63,64,65,72,73,74]))

        return map(lambda x: x.get(), filter(lambda x: x.is_constante(), tmp))

    def find_cell_possible(self, grid, posx, posy):
        cell = grid.get(posx, posy)

        notPossibletmp = self.get_vertical_line(grid, posx, posy)
        notPossibletmp.extend(self.get_horizontal_line(grid, posx, posy))
        notPossibletmp.extend(self.get_grid_line(grid, posx, posy))
        notPossible = set(notPossibletmp)

        return filter(lambda x: not x in notPossible , range(1,10))


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
               