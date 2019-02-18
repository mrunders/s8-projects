import numpy as np 
import pandas

from sklearn.model_selection import train_test_split

sigmoid = lambda x : 1 / (1 + np.exp(-x))
sigmoid_deriv = lambda x : x * (1 - x)

eta = 0.05 ## default 0.01

## err_func
def quadradique(yt, yp): return (yp - yt)**2
def absolut(yt, yp): return abs(yt - yp)
def zero_one(yt, yp): return 0 if yt == yp else 1

## prediction_func
def simple_dot(w,X): return np.dot(w,X)
def internet_p(w,X): return sigmoid(np.dot(X.astype(float), w))

## update_weights
def course_update(w,X,yt,yp): return w - (eta/2) * (yp - yt) * X
def internet_u(w,X,yt,yp): return w + np.dot(x.T, (yt - yp) * sigmoid_deriv(yp))

## default_weights
def npzeros(size): return np.zeros(size)
def lizeros(size): return [0 for _ in size]


CROSS_VALIDATION_POURCENTAGE = 0.1

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