import numpy as np 

from libs import *

class LearningClass(object):

    def __init__(self, default_weights, update_weights, predictions_func, err_func=quadradique):

        np.random.seed(1)
        self.err_func = err_func
        self.weights = np.array(default_weights)
        self.update_weights = update_weights
        self.predictions_func = predictions_func
    
    def train(self, Xt, yt, iterations):

        iteration = -1
        for _ in range(iterations):
            for x,y in zip(Xt,yt):
                yp = self.think(x)
                self.weights = self.update_weights(self.weights, x, y, yp)
                iteration += 1
                yield self.think, iteration
    
    def think(self, X):
        return self.predictions_func(self.weights, X)

    def error(self, yt, yp):
        return self.err_func(yt, yp)
