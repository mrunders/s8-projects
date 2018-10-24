
from math import log as log
from operator import mul as mul

import numpy as np

ALPHA = 0.01

X=[1,2,4,3,5]
Y = [1,3,3,2,5]

XX1 = [2.78,1.46,3.39,1.38,3.06,7.62,5.33,6.92,8.67,7.67]
XX2 = [2.55,2.36,4.40,1.85,3.00,2.75,2.08,1.77,-0.24,3.50]
YY = [0,0,0,0,0,1,1,1,1,1]

XXX = [4.66,5.50,4.70,5.95,5.73,5.02,4.80,4.42,5.00,5.11,6.37,2.89,4.66,5.60,4.90,5.03,4.08,4.87,4.73,5.38,20.74,\
21.41,20.57,20.73,19.44,18.36,19.90,19.10,18.18,19.71,19.09,20.52,20.63,19.86,21.34,20.33,21.02,18.27,21.77,20.65]
YYY = [0 for i in range(20), 1 for i in range(20)]

#############################################################
## 
##  > Logic regrassion with probability
##
#############################################################


def discrimine(x, k=20):

    if not type(x) is np.array:
        x = np.array(x)

    u = x.mean()
    o = x.var()
    return x * (u/o**2) - (u**2/2*(o**2)) + log(0.5)

#############################################################
## 
##  > Generic Gradient descent Algorithm
##
#############################################################

def p_i2(beta, x):
    return sum(map(mul, beta, x))

def e_i2(beta, x):
    return 1 / ( 1 + math.exp(-p_i2(beta,x)))

def gradient_descent_n(xarrays, yarrays, func, default_beta_values=0, max_iterations=20, alpha=0.01):

    iteration = 0

    xarrays = zip(*xarrays)
    for xx in range(len(xarrays)):
        xarrays[xx] = list(xarrays[xx])
        xarrays[xx].insert(0, 1)
    
    beta = [0 for i in xarrays[0]]
    
    print("Gradient Descent with values: X={}, Y={}, ALPHA={}".format(xarrays,yarrays,alpha))
    while(True):
        for i in range(len(yarrays)):

            if iteration == max_iterations:
                return

            p_i = func(beta, xarrays[i])

            error =  p_i - yarrays[i]
            ##error = (yarrays[i] - p_i) * p_i * ( 1 - p_i )

            for b in range(len(beta)):
                beta[b] = beta[b] - error * xarrays[i][b] * alpha

            iteration += 1
            print(("Iteration: %3d | erreur:%20f Beta: {}" % (iteration, error)).format(beta) )       

## gradient_descent_n(xarrays=[XX1, XX2], yarrays=YY, default_beta_values=0, max_iterations=20, alpha=0.01, func=p_i2)
print(discrimine(x=XXX))