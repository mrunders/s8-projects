
import numpy
import pandas

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

from sklearn.datasets import load_boston  # boston.data, boston.target

from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_recall_curve

from GradientDescent import gradient_descent_n as gradient
from GradientDescent import p_i2 as gd_func

from sklearn import datasets
from sklearn import svm

INF_4 = 0
SUP_4 = 1

COURTE = 0
MOYENE = 1
LONGUE = 2

INF_150 = 0
SUP_150 = 1

OUI = 1
NON = 0

datasetClassX = pandas.DataFrame({
    'Memory': [INF_4,SUP_4,SUP_4,INF_4,SUP_4,SUP_4,INF_4,INF_4,SUP_4,INF_4,INF_4,SUP_4,INF_4,SUP_4,SUP_4,INF_4],
    'Battery': [LONGUE,LONGUE,LONGUE,LONGUE,LONGUE,COURTE,COURTE,COURTE,COURTE,COURTE,MOYENE,MOYENE,MOYENE,MOYENE,MOYENE,MOYENE],
    'Price': [INF_150,SUP_150,INF_150,SUP_150,SUP_150,SUP_150,SUP_150,SUP_150,INF_150,INF_150,INF_150,INF_150,SUP_150,SUP_150,INF_150,SUP_150]
})

dataSetClassY = pandas.DataFrame({
    'Happy': [OUI,OUI,OUI,OUI,OUI,OUI,NON,NON,OUI,NON,NON,NON,OUI,OUI,NON,OUI]
})  

def nonLinearAlgorithme(xset, yset, data_split_size=0.5):

    regressor = DecisionTreeClassifier()
    xtrain,xtest,ytrain,ytest = train_test_split(xset,yset, test_size=data_split_size, random_state=0)
    regressor.fit(xtrain,ytrain)

    ## print(regressor.predict_proba(xtest))
    precision, recal, f1 = precision_recall_curve(ytrain, ytest)
    return {'precision': precision, 'recal': recal, 'f1': f1}


def linearAlgorithme(xset, yset, data_split_size=0.5):

    xtrain,xtest,ytrain,ytest = train_test_split(xset,yset, test_size=data_split_size, random_state=0)

    clf = svm.SVC(kernel='linear', C=1).fit(xtrain, ytrain)
    return clf.score(xtest, ytest)

## print(nonLinearAlgorithme(datasetClassX,dataSetClassY))
## print(linearAlgorithme(datasetClassX,dataSetClassY))