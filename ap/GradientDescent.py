
import math

p_i = (lambda b0,b1,b2,x1,x2 : b0 + b1 * x1 + b2 * x2)
e_i = (lambda b0,b1,b2,x1,x2 : 1 / ( 1 + math.exp(-p_i(b0,b1,b2,x1,x2))))
ALPHA = 0.01

X=[1,2,4,3,5]
Y = [1,3,3,2,5]

XX1 = [2.78,1.46,3.39,1.38,3.06,7.62,5.33,6.92,8.67,7.67]
XX2 = [2.55,2.36,4.40,1.85,3.00,2.75,2.08,1.77,-0.24,3.50]
YY = [0,0,0,0,0,1,1,1,1,1]

XXX = [4.66,5.50,4.70,5.93,5.73,5.02,4.80,4.42,5.11,6.37,2.89,4.66,5.60,4.90,5.03,4.08,4.87,4.73,5.38,20.74,21.41,20.57,20.73,19.44,18.36,19.90,19.10,18.18,19.71,19.09,20.52,20.66,19.86,21.34,20.33,21.02,18.27,21.77,20.65]
YYY = [0 for i in range(20)]
YYY.extend([1 for i in range(20)])

def mean_value(x, n=20):
    return (1 / n) * sum(x)

def variance(x, u, n=40, K=2):
    s = 0
    for xx in x:
        s += (xx - mean_value(x))**2
    
    return (1 / (n-K)) * s

def discrimine(x, k=20):
    u = mean_value(x)
    o = variance(x,u)
    return x * (u/o**2) - (u**2/2*o**2) + math.log(1/2)

def gd_2d(max_iterations=20, b0=0, b1=0):

    iteration = 0
    
    print("Gradient Descent with values: X={}, Y={}, ALPHA={}".format(X,Y,ALPHA))
    while(True):
        for i in range(len(X)):

            if iteration == max_iterations:
                return

            x = X[i]
            y = Y[i]
            error = p_i(b0,b1,0,x1,0) - y
            b0 = b0 - error * x * ALPHA
            b1 = b1 - error * ALPHA

            iteration += 1
            print("Iteration: %3d | erreur=%20f b0=%20f , b1=%20f" % \
            (iteration, error, b0, b1))

def gd_3d(max_iterations=20, b0=0, b1=0, b2=0, func=p_i):

    iteration = 0

    print("Gradient Descent with values: X1={}, X2={}, Y={}, ALPHA={}".format(XX1,XX2,YY,ALPHA))
    while(True):
        for i in range(len(XX1)):

            if iteration == max_iterations:
                return

            x1 = XX1[i]
            x2 = XX2[i]
            y = YY[i]

            p = func(b0,b1,b2,x1,x2)
            error = (y - p) * p * ( 1 - p )
            b0 = b0 - error * ALPHA
            b1 = b1 - error * x1 * ALPHA
            b2 = b2 - error * x2 * ALPHA			

            iteration += 1
            print("Iteration: %3d | erreur=%20f b0=%20f , b1=%20f, b2=%20f" % \
            (iteration, error, b0, b1, b2))
