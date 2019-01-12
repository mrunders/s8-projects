import platform

if platform.system() == "Windows":
    from Tkinter import *
else :
    from tkinter import *

class Case():

    def __init__(self, indice):

        self.test_node = False

        if indice == None:
            self.indice = list()
        elif type(indice) == int:
            self.indice = [indice]
        elif type(indice) == list:
            self.indice = indice
        else:
            raise "No matched type exception"

    def get(self):
        return self.indice[0]

    def get_all(self):
        return self.indice

    def is_none(self):
        return len(self.indice) == 0

    def is_constante(self):
        return len(self.indice) == 1 and not self.test_node

    def is_tmp(self):
        return len(self.indice) > 1

    def __str__(self):
        if self.is_none():
            return " "

        return str(self.indice)[1:-1]

    def notify(self, possible):

        if self.is_constante():
            return

        self.test_node = True
        self.indice = possible

    def commit_changes(self):
        self.test_node = False

class CaseGui(Frame, object):

    def __init__(self, parent, case):
        super(CaseGui, self).__init__(parent, relief=GROOVE)
        self.case = case

        self.label = Label(self, text="", padx=1, pady=1, relief=GROOVE, width=10, height=5)
        self.notify()

        self.label.pack()

    def notify(self):

        self.case.commit_changes()

        if self.case.is_constante():
            self.label.config(bg="#008000", text=self.case)
        elif self.case.is_tmp():
            self.label.config(bg="#505050", text=self.case)
        else:
            self.label.config(bg="#FFFFFF", text=self.case)