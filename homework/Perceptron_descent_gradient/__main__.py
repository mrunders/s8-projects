
import pandas
import numpy

from math import floor
from random import randint
from GradientDescent import *
from Perceptron import *

from matplotlib import pyplot as plt

from sklearn.model_selection import train_test_split

CROSS_VALIDATION_POURCENTAGE = 0.1

IRIS_HEADER = ["Sepal lenght", "Sepal width", "Petal lenght", "Petal width", "Iris"]
IRIS_DATA   = "iris_data.gob"

class Plot_builder():

    def __init__(self, save_pas=10):
        self.save_pas = save_pas
        self.pas = 0
        self.x_plot = list()
        self.y_plot = list()
        self.plt = plt

    def savable(self):
        self.pas += 1
        if self.pas == self.save_pas:
            self.pas = 0
            return True

        return False

    def save(self, xplot, yplot):
        self.x_plot.append(xplot)
        self.y_plot.append(yplot)

    def draw_plot(self, name, max_x, color="b", xlabel="", ylabel=""):
        self.plt.plot(self.x_plot, self.y_plot, color, linewidth=0.8, marker=".")
        self.plt.axis([0, max_x, 0, 1])
        self.plt.ylabel(ylabel)
        self.plt.xlabel(xlabel)

    def show_plot(self):
        plt.show()


class Data():

    @staticmethod
    def read_data(path, header):
        return pandas.read_csv(path, names=header)

    @staticmethod
    def shuffle(dataset):
        return dataset.iloc[np.random.permutation(len(dataset))]

    @staticmethod
    def iloc(dataset):
        return dataset.iloc[:,:-1], dataset.iloc[:,-1] ## X, y

    @staticmethod
    def train_test_split(X, y):
        return train_test_split(X, y, test_size=CROSS_VALIDATION_POURCENTAGE, random_state=0)

    @staticmethod
    def format_y_to_list(y):
        yfinal = y.tolist()
        ylist = list(set(yfinal))
        for ind,elt in enumerate(yfinal):
            yfinal[ind] = ylist.index(elt)

        return yfinal

    @staticmethod
    def format_X_to_list(X):
        return X.values

class PerceptronAlgo():

    def __init__(self, data_path, data_header, plot_builder_save_pas=10, error_func=quadradique):
        self.plt = Plot_builder(save_pas=plot_builder_save_pas)
        self.dataset = Data.read_data(data_path, data_header)
        self.dataset = Data.shuffle(self.dataset)
        self.X, self.y = Data.iloc(self.dataset)
        self.X = Data.format_X_to_list(self.X)
        self.y = Data.format_y_to_list(self.y)
        self.Xtrain, self.Xtest, self.ytrain, self.ytest = Data.train_test_split(self.X, self.y)
        self.perceptron = Perceptron(default_weights=list(repeat(0, len(self.Xtrain[0]))))
        self.error_func = error_func

    def run(self, nb_iterations):
        for think_function, iteration in self.perceptron.train(self.Xtrain, self.ytrain, nb_iterations):
            if self.plt.savable():
                good_predictions = 0
                for i in range(len(self.ytest)):
                    xtest, ytest = self.Xtest[i], self.ytest[i]
                    ypred = think_function(xtest)
                    good_predictions += self.error_func(ytest, ypred)

                self.plt.save(iteration, good_predictions / (0.0 + i))

    def get_plot(self):
        return self.plt



p = PerceptronAlgo(IRIS_DATA, IRIS_HEADER)
p.run(4500)
pl = p.get_plot()
pl.draw_plot("perceptron iris", max_x=4500)
pl.show_plot()
