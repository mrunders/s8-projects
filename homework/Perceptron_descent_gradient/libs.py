################################################################
##
## DEFAULT_WEIGHTS are all way used to initialise the weights array
##
## Data contains all usefull function to pasrse the data
##
##################################################################


import numpy as np 
import pandas

from sklearn.model_selection import train_test_split

CROSS_VALIDATION_POURCENTAGE = 0.1
IRIS_TRUE_VALUE = "Iris-versicolor"


TMP = [5,101,28,89,26,72,25,139,119,13,3,143,80,75,77,69,93,76
,8,10,43,114,23,9,116,35,134,53,96,131,40,145,144,87,14,39
,130,27,50,85,30,16,108,1,15,2,51,121,97,38,24,140,32,60
,68,49,21,78,0,83,33,54,124,120,82,84,107,106,112,132,62,133
,109,138,64,44,58,37,66,147,142,7,19,148,47,137,127,48,79,59
,22,146,111,36,117,29,122,136,46,41,52,88,56,110,141,118,103,128
,11,90,67,63,149,86,20,61,73,31,70,129,74,6,113,71,98,34
,95,4,126,81,45,100,18,94,123,12,99,91,105,104,115,102,125,65
,135,55,92,42,17,57]

class Data():

    @staticmethod
    def read_data(path, header):
        return pandas.read_csv(path, names=header)

    @staticmethod
    def shuffle(dataset):
        return dataset.iloc[np.random.permutation(len(dataset))]
        ##return dataset.iloc[TMP]

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
    def format_iris_y_to_list(y):
        yfinal = y.tolist()
        for ind,elt in enumerate(yfinal):
            yfinal[ind] = 1 if elt == IRIS_TRUE_VALUE else -1

        return yfinal

    @staticmethod
    def format_X_to_list(X):
        return X.values