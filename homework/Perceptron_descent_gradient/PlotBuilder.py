
from matplotlib import pyplot as plt

class Plot_builder():

    def __init__(self):
        self.x_plot = list()
        self.y_plot = list()
        self.plt = plt

    def save(self, xplot, yplot):
        self.x_plot.append(xplot)
        self.y_plot.append(yplot)

    def draw_plot(self, name, max_x, color="b", xlabel="trial", ylabel="error"):
        self.plt.plot(self.x_plot, self.y_plot, color, linewidth=0.5)
        self.plt.axis([0, max_x, 0, 1.1])
        self.plt.title(name)
        self.plt.ylabel(ylabel)
        self.plt.xlabel(xlabel)

    def show_plot(self):
        plt.show()