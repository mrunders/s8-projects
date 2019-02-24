
import numpy

from AlgoClass import *
from PlotBuilder import Plot_builder

from libs import *

class Algo(object):

    def __init__(self, X, y, algo, yielding_pas=10, shuffle_data=True, gradient_eta=None):

        self.plt = Plot_builder()
        self.Xtrain, self.Xtest, self.ytrain, self.ytest = Data.train_test_split(X, y)

        if gradient_eta != None and algo == GradientDescent:
            self.algo = algo(default_weights=np.zeros(len(self.Xtrain[0])), yielding_pas=yielding_pas, eta=gradient_eta)
        else:
            self.algo = algo(default_weights=np.zeros(len(self.Xtrain[0])), yielding_pas=yielding_pas)

    def run(self, nb_iterations):

        len_yset = len(self.ytest)
        for think_function, iteration in self.algo.train(self.Xtrain, self.ytrain, nb_iterations):
            good_predictions = 0
            for i in range(len_yset):
                good_predictions += self.algo.error(self.ytest[i], think_function(self.Xtest[i]))

            avg_errors_predictions = (good_predictions) / (0.0 + len_yset)
            ###print("goods predictions %d / %d, wrongs predictions %f" % (good_predictions, len_yset, avg_errors_predictions))
                    
            self.plt.save(iteration, avg_errors_predictions)

    def get_plot(self):
        return self.plt



MAX_PLOT_X = 4500

iris_X, iris_y = Data.load_iris_data()
perceptron = Algo(iris_X, iris_y, algo=Perceptron, yielding_pas=10, shuffle_data=True)
perceptron.run(nb_iterations=MAX_PLOT_X)
perceptron_plot = perceptron.get_plot()
perceptron_plot.draw_plot(name="perceptron iris", max_x=MAX_PLOT_X)
perceptron_plot.show_plot()

"""
gradient_descent = Algo(iris_X, iris_y, algo=GradientDescent, yielding_pas=10, shuffle_data=True, gradient_eta=2)
gradient_descent.run(nb_iterations=MAX_PLOT_X)
gradient_descent_plot = gradient_descent.get_plot()
gradient_descent_plot.draw_plot(name="gradient descent iris", max_x=MAX_PLOT_X)
gradient_descent_plot.show_plot()
"""