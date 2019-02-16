import numpy as np 

sigmoid = lambda x : 1 / (1 + np.exp(-x))
sigmoid_deriv = lambda x : x * (1 - x)

quadradique = lambda yt, yp : (yt - yp)**2
absolut     = lambda yt, yp : abs(yt - yp)
zero_one    = lambda yt, yp : 0 if yt == yp else 1

default_weights = lambda x : 2 * np.random.random((x, 1)) - 1

class LearningClass(object):

    def __init__(self):
        pass

    def think(self, x):
        raise NotImplementedError()

class Perceptron(LearningClass):

    def __init__(self, default_weights=0, err_func=quadradique):
        super(Perceptron, self).__init__()

        np.random.seed(1)
        self.err_func = err_func
        self.weights = default_weights
    
    def train(self, Xt, yt, iterations):

        for i in range(iterations):
            yp = self.think(Xt)
            self.weights += np.dot(Xt.T, self.err_func(yt, yp) * sigmoid_deriv(yp))
            yield self.think, i
    
    def think(self, X):
        return sigmoid(np.dot(X.astype(float), self.weights))

"""
p = Perceptron(default_weights=default_weights)

x = np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
yt = np.array([[0,1,1,0]]).T

p.train(x, yt, 15000)
"""
