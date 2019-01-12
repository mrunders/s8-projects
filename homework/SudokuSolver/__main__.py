
import platform

if platform.system() == "Windows":
    from Tkinter import *
else :
    from tkinter import *

from Grid import *
from Case import *
from Solver import *

class GrilleGui(Frame, object):

    def __init__(self, file_reader):
        self.fenetre = Tk()
        super(GrilleGui, self).__init__(self.fenetre)

        self.fenetre.title('Sudoku Solver Project')
        self.fenetre.geometry("800x800")
        self.fenetre.resizable(0, 0)

        self.grid = GrilleGui.read_grid(file_reader)
        self.gridGui = map(lambda x: CaseGui(self, x), self.grid.get())

        self.next_state = Button(self.fenetre, text="Next state", command=self.solve_find_cell_possible)
        self.validation = Button(self.fenetre, text="validation", command=self.validation)

        pos_x, pos_y = 0,0
        for case_gui in self.gridGui:

            if pos_x == 9:
                pos_x = 0
                pos_y += 1
            case_gui.grid(row=pos_y, column=pos_x)
            pos_x += 1

        self.pack()
        self.next_state.pack()
        self.validation.pack()
        self.fenetre.mainloop()

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
        print(self.grid.validation())
        


g = GrilleGui("sudoku_medium.txt")