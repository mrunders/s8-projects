import numpy as np 


def sign(y):
    return -1 if y < 0 else 1

class Perceptron():

    def __init__(self, default_weights, yielding_pas):

        self.weights = np.array(default_weights)
        self.yielding_pas = yielding_pas

    @staticmethod
    def __false_prediction(w, x, yp):
        return (np.dot(w,x) * yp) <= 0

    @staticmethod
    def __update_weights(w, yt, x):
        return w + yt * x
    
    def train(self, Xt, yt, iterations):

        iteration_number = 0
        yield self.think, iteration_number

        tmp_zip = zip(Xt, yt)
        len_zip = len(tmp_zip)
        while iteration_number < iterations:

            for _ in range(self.yielding_pas):

                x,y = tmp_zip[iteration_number % len_zip]
                yp = self.think(x)

                if Perceptron.__false_prediction(self.weights, x, yp):
                    self.weights = Perceptron.__update_weights(self.weights, x, y)

                iteration_number += 1

            yield self.think, iteration_number
    
    def think(self, x):
        return np.dot(self.weights, x)

    def error(self, yt, yp):
        return 0 if yt == sign(yp) else 1

class GradientDescent():

    def __init__(self, default_weights, yielding_pas, eta=10):
    
        self.eta = eta
        self.tmp_weights = np.array(default_weights)
        self.weights = np.array(default_weights)
        self.yielding_pas = yielding_pas

    @staticmethod
    def __false_prediction(w,x, yp):
        return (np.dot(w,x) * yp) < 1

    @staticmethod
    def __update_weights(w, yt, x):
        return w + yt * x    

    def train(self, Xt, yt, iterations):

        iteration_number = 0
        yield self.think, iteration_number

        tmp_zip = zip(Xt, yt)
        len_zip = len(tmp_zip)
        while iteration_number < iterations:

            for _ in range(self.yielding_pas):

                x,y = tmp_zip[iteration_number % len_zip]
                tmp_weights = (1 / self.eta) * self.weights
                yp = self.__tmp_think(x)

                if GradientDescent.__false_prediction(self.weights, x, yp):
                    self.weights = GradientDescent.__update_weights(self.weights, x, y)

                iteration_number += 1

            yield self.think, iteration_number

    def __tmp_think(self, x):
        return np.dot(self.tmp_weights, x)
    
    def think(self, x):
        return np.dot(self.weights, x)

    def error(self, yt, yp):
        return 0 if yt == sign(yp) else 1