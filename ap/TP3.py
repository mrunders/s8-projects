import numpy
import csv
import urllib

from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, LeaveOneOut
from sklearn.model_selection import ShuffleSplit

from sklearn.metrics import accuracy_score, log_loss, roc_curve, confusion_matrix, classification_report
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

DEFAULT_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
COLUMNS_DELIMITER = ','
DEFAULT_COLUMNS_HEADER = ["number", "Clump Thickness", \
"Uniformity of Cell Size", "Uniformity of Cell Shape", \
"Marginal Adhesion", "Single Epithelial Cell Size", \
"Bare Nuclei", "Bland Chromatin", "Normal Nucleoli", \
"Mitoses", "Class"]

def getFluxFromUrl(url):
    return urllib.urlopen(url)

def getFluxFromFIle(dirr):
    return open(dirr)

def closeFlux(flux):
    flux.close()

def fluxToStringIO(flux):
    return (COLUMNS_DELIMITER.join(i) for i in csv.reader(flux))

def stringIOToNumpyArray(str):
    return numpy.genfromtxt(str, delimiter=COLUMNS_DELIMITER, dtype=numpy.float64)

def urlToNumpyArray(url=DEFAULT_URL):
    return stringIOToNumpyArray(fluxToStringIO(getFluxFromUrl(url)))

def fileToNumpyArray(file):
    return stringIOToNumpyArray(fluxToStringIO(getFluxFromFIle(file)))

def x_ySplit(array):
    return numpy.hsplit(array, [1, 13])

## Evaluation
def eval_traintest(*args):
    return train_test_split(*args)

def eval_kfold(x_array, y_array):
    kf = KFold(n_splits=2)
    x_train, y_train, x_test, y_test = list(), list(), list(), list()
    for train_i,test_i in kf.split(x_array):
        x_train.append(x_array[train_i])
        x_test.append(x_array[test_i])
        y_train.append(y_array[train_i])
        y_test.append(y_array[test_i])
    
    return x_train, x_test, y_train, y_test

def eval_leaveOneOut(x_array, y_array):
    kf = LeaveOneOut()
    x_train, y_train, x_test, y_test = list(), list(), list(), list()
    for train_i,test_i in kf.split(x_array):
        x_train.append(x_array[train_i])
        x_test.append(x_array[test_i])
        y_train.append(y_array[train_i])
        y_test.append(y_array[test_i])
    
    return x_train, x_test, y_train, y_test

def eval_random_split(x_array, y_array):
    kf = ShuffleSplit(n_splits=5, test_size=.25, random_state=0)
    test, train = list(), list()
    for train_i, test_i in kf.split(x_array):
        test.append(test_i)
        train.append(train_i)
    
    return train, test

## Performance Metrics
def accuracy(y_p, y_t, normalized=False):
    return accuracy_score(y_t, y_p, normalize=normalized)

def logloss(y_p, y_t):
    return log_loss(y_p, y_t)

def roc_curve(y_p, y_t):
    return roc_curve(y_t, y_p, pos_label=2)

def matrice_confusion(y_p, y_t):
    return confusion_matrix(y_t, y_p)

def classification(y_p, y_t, target_names):
    return classification_report(y_t, y_p, target_names=target_names)

def absolute_error(y_p, y_t, multioutput=None):
    return mean_absolute_error(y_t, y_p, multioutput=multioutput)

def squared_error(y_p, y_t):
    return mean_squared_error(y_t, y_p)

def r2score(y_p, y_t, multioutput=None):
    return r2_score(y_t, y_p, multioutput=multioutput)


array = urlToNumpyArray()
y_array, x_array = x_ySplit(array)
