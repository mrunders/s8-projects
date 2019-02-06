import numpy as np 

from copy import deepcopy

sigmoid = lambda x : 1 / (1 + np.exp(-x))
sigmoid_deriv = lambda x : x * (1 - x)

quadradique = lambda yt, yp : (yt - yp)**2
absolut     = lambda yt, yp : abs(yt - yp)
zero_one    = lambda yt, yp : 0 if yt == yp else 1

default_weights = lambda x : 2 * np.random.random((x, 1)) - 1

class Perceptron():

    def __init__(self, default_weights=0, err_func=quadradique):

        np.random.seed(1)
        self.err_func = err_func
        self.default_weights = default_weights
    
    def train(self, x, yt, it):

        self.weights = self.default_weights(len(x[0]))
        for i in range(it):
            yp = self.think(x)
            self.weights += np.dot(x.T, self.err_func(yt, yp) * sigmoid_deriv(yp))
    
    def think(self, x):
        return sigmoid(np.dot(x.astype(float), self.weights))


p = Perceptron(default_weights=default_weights)

x = np.array([[0,0,1],[1,1,1],[1,0,1],[0,1,1]])
yt = np.array([[0,1,1,0]]).T

p.train(x, yt, 15000)

def all_combinaisons(domain=[0,1], arite=1):

    if arite == 1:
        return [[x] for x in domain]

    else:
        part = all_combinaisons(domain=domain, arite=arite-1)
        final = []
        for x in domain:
            tmp = deepcopy(part)
            for l in tmp:
                l.insert(0,x)
            final.extend(tmp)

        return final


for i,j,k in all_combinaisons(arite=3):
    print("(%d,%d,%d) -> %s" % (i,j,k,p.think(np.array([i,j,k]))))
