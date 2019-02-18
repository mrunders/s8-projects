
import numpy

from AlgoClass import LearningClass
from PlotBuilder import Plot_builder

from libs import *

IRIS_HEADER = ["Sepal lenght", "Sepal width", "Petal lenght", "Petal width", "Iris"]
IRIS_DATA   = "iris_data.gob"

class Algo(object):

    def __init__(self, data_path, data_header, update_weights, predictions_func, err_func, plot_builder_save_pas=10, shuffle_data=True):

        self.plt = Plot_builder(save_pas=plot_builder_save_pas)
        self.dataset = Data.read_data(data_path, data_header)

        if shuffle_data:
            self.dataset = Data.shuffle(self.dataset)

        self.X, self.y = Data.iloc(self.dataset)
        self.X = Data.format_X_to_list(self.X)
        self.y = Data.format_y_to_list(self.y)
        self.Xtrain, self.Xtest, self.ytrain, self.ytest = Data.train_test_split(self.X, self.y)

        self.err_func = err_func
        self.shuffle_data = shuffle_data
        self.update_weights = update_weights
        self.predictions_func = predictions_func
        self.plot_builder_save_pas = plot_builder_save_pas

        self.algo = LearningClass(default_weights=npzeros(len(self.Xtrain[0])), 
                update_weights=update_weights, predictions_func=predictions_func, err_func=err_func)

    def run(self, nb_iterations):
        for think_function, iteration in self.algo.train(self.Xtrain, self.ytrain, nb_iterations):
            if self.plt.savable():
                good_predictions = 0
                for i in range(len(self.ytest)):
                    xtest, ytest = self.Xtest[i], self.ytest[i]
                    ypred = think_function(xtest)
                    good_predictions += self.algo.error(ytest, ypred)

                self.plt.save(iteration, good_predictions / (0.0 + len(self.ytest)))

    def get_plot(self):
        return self.plt

    def __str__(self):
        return "Algo: %s, plot_builder save pas: %d, shuffled data: %s, error func: %s, update weights: %s, predictions func: %s" %\
        (self.__name__(), self.plot_builder_save_pas,  self.shuffle_data, self.err_func.__name__, self.update_weights.__name__, self.predictions_func.__name__)

class PerceptronAlgo(Algo):

    def __init__(self, data_path, data_header, plot_builder_save_pas, shuffle_data=True, err_func=zero_one, update_weights=course_update, predictions_func=simple_dot):
        super(PerceptronAlgo, self).__init__(data_path, data_header, err_func=err_func, plot_builder_save_pas=plot_builder_save_pas, 
                                            update_weights=update_weights, predictions_func=predictions_func, shuffle_data=shuffle_data)

    def __name__(self):
        return "Perceptron"

class GradientDescentAlgo(Algo):

    def __init__(self, data_path, data_header, plot_builder_save_pas, shuffle_data=True, err_func=quadradique, update_weights=course_update, predictions_func=simple_dot):
        super(GradientDescentAlgo, self).__init__(data_path, data_header, err_func=err_func, plot_builder_save_pas=plot_builder_save_pas, 
                                            update_weights=update_weights, predictions_func=predictions_func, shuffle_data=shuffle_data)

    def __name__(self):
        return "Gradient Descent"

p = PerceptronAlgo(data_path=IRIS_DATA, data_header=IRIS_HEADER, plot_builder_save_pas=10, shuffle_data=True)
print(p)
p.run(nb_iterations=100)
pl = p.get_plot()
pl.draw_plot(name="perceptron iris", max_x=14000)
pl.show_plot()


q = GradientDescentAlgo(data_path=IRIS_DATA, data_header=IRIS_HEADER, plot_builder_save_pas=10, shuffle_data=True)
print(q)
q.run(nb_iterations=100)
ql = q.get_plot()
ql.draw_plot(name="gradient descent iris", max_x=14000)
ql.show_plot()
