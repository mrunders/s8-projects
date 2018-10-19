
import csv
import urllib
import numpy
import pandas

DEFAULT_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data"
COLUMNS_DELIMITER = ','
DEFAULT_COLUMNS_HEADER = ["number", "Clump Thickness", \
"Uniformity of Cell Size", "Uniformity of Cell Shape", \
"Marginal Adhesion", "Single Epithelial Cell Size", \
"Bare Nuclei", "Bland Chromatin", "Normal Nucleoli", \
"Mitoses", "Class"]
DEFAULT_COLUMNS_DTYPE = {0: numpy.float64}

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

def loadCsvPandas(str):
    return pandas.read_csv(str, delimiter=COLUMNS_DELIMITER, dtype=DEFAULT_COLUMNS_DTYPE, header=None)

#### Complet functions
def urlToNumpyArray(url=DEFAULT_URL):
    return stringIOToNumpyArray(fluxToStringIO(getFluxFromUrl(url)))

def fileToNumpyArray(file):
    return stringIOToNumpyArray(fluxToStringIO(getFluxFromFIle(file)))

def urlToPandas(url=DEFAULT_URL):
    return loadCsvPandas(getFluxFromUrl(url))

def fileToPandas(file):
    return loadCsvPandas(getFluxFromFIle(file))

def getNHeadsPandasRows(ml_data, n):
    assert type(ml_data) is pandas.core.frame.DataFrame
    return ml_data.head(n=n)

def shape(ml_data):
    return ml_data.shape

def renameColumns(ml_data, columns_header=DEFAULT_COLUMNS_HEADER):

    if ( shape(ml_data)[1] != len(columns_header) ):
        print(" ml_data columns number is not equal to given header ")
        raise 

    return ml_data.rename( columns=dict([k,v] for k,v in enumerate(columns_header)) )

def getDataTypes(ml_data):
    return ml_data.dtypes

def getStats(ml_data, column=None, stat=None):

    stats = ml_data.describe() if column is None else ml_data[column].describe()
    return stats if stat is None else stats[stat]





def getqd():
    return renameColumns(getNHeadsPandasRows(urlToPandas(), 8))