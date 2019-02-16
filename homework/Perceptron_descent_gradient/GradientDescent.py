
from math import log as log
from operator import mul as mul
from itertools import repeat

import numpy as np


ALPHA = 0.01

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
    return 1 / ( 1 + np.exp(-p_i2(beta,x)))

def gradient_descent_n(xarrays, yarrays, func, default_beta_values=0, max_iterations=20, alpha=0.01, print_infos=False):

    iteration = 0

    xarrays = zip(*xarrays)
    for xx in range(len(xarrays)):
        xarrays[xx] = list(xarrays[xx])
        xarrays[xx].insert(0, 1)
    
    beta = repeat(0, xarrays[0])
    
    if print_infos:
        print("Gradient Descent with values: X={}, Y={}, ALPHA={}".format(xarrays,yarrays,alpha))

    while(True):
        for i in range(len(yarrays)):

            if iteration == max_iterations:
                return

            p_i = func(beta, xarrays[i])
            error =  p_i - yarrays[i]

            for b in range(len(beta)):
                beta[b] = beta[b] - error * xarrays[i][b] * alpha

            iteration += 1
            if print_infos:
                print(("Iteration: %3d | erreur:%20f Beta: {}" % (iteration, error)).format(beta))       

## gradient_descent_n(xarrays=[XX1, XX2], yarrays=YY, default_beta_values=0, max_iterations=20, alpha=0.01, func=p_i2)