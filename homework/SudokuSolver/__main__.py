
import platform

if platform.system() == "Windows":
    from Tkinter import *
else :
    from tkinter import *

from Grid import *
from Case import *
from Solver import *

class GrilleGui(Frame, object):

    def __init__(self, parent, file_reader):
        super(GrilleGui, self).__init__(parent, padx=20)

        self.grid = GrilleGui.read_grid(file_reader)
        self.gridGui = map(lambda x: CaseGui(self, x), self.grid.get())

        pos_x, pos_y = 0,0
        for case_gui in self.gridGui:

            if pos_x == 9:
                pos_x = 0
                pos_y += 1
            case_gui.grid(row=pos_y, column=pos_x)
            pos_x += 1

    @staticmethod
    def read_grid(file_reader):

        if type(file_reader) == list:
            return Grille(file_reader)
        
        elif type(file_reader) == str:
            with open(file_reader, "r") as file:
                res = map(lambda x: None if x == 'None' else int(x), file.read().split())

            return Grille(res)

    def getGrid(self):
        return self.grid
    
    def solve_find_cell_possible(self):
        self.grid.solve_find_cell_possible()
        for case_gui in self.gridGui:
            case_gui.notify()
    
    def validation(self):
        return self.grid.validation()

    def swapGrid(self, new_grid):
        for i in range(len(new_grid)):
            self.gridGui[i].swap(new_grid[i])
            self.gridGui[i].notify()

    def getState(self):
        return self.grid.getState()

class SudokuSolver(Frame, object):

    def __init__(self, file_descriptor):
        self.fenetre = Tk()
        super(SudokuSolver, self).__init__(self.fenetre, padx=50)

        self.fenetre.title('Sudoku Solver Project')
        self.fenetre.geometry("1000x800")
        self.fenetre.resizable(0, 0)

        self.previous_grid = GrilleGui(self, file_descriptor)
        self.current_grid = GrilleGui(self, file_descriptor)

        self.next_state = Button(self.fenetre, text="next state", command=self.solve_find_cell_possible)
        self.is_solved = Label(self.fenetre, text="Is Solved?: %10s" % (" "))
        self.state = Label(self.fenetre, text="Current heristique %30s" % ("WAITING"))

        self.pack()

        ##self.previous_grid.pack(side=LEFT)
        self.current_grid.pack(side=RIGHT)

        self.state.pack(side=TOP)
        self.next_state.pack(side=RIGHT)
        self.is_solved.pack(side=BOTTOM)

        self.fenetre.mainloop()

    def solve_find_cell_possible(self):
    
        self.state.config(text="Current heristique %30s" % (self.current_grid.getState()))
        self.previous_grid.swapGrid(self.current_grid.getGrid().get())
        self.current_grid.solve_find_cell_possible()
        self.is_solved.config(text="Is Solved?: %10s" % (self.validation()))

    def validation(self):
        return self.current_grid.validation()

g = SudokuSolver("demoniac.txt")
