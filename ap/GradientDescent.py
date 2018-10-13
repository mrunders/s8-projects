
X = [1,2,4,3,5]
Y = [1,3,3,2,5]

ALPHA = 0.01

def gd(max_iterations=20, b0=0, b1=0):

    iteration = 0
    while(True):
        for i in range(len(X)):

            if iteration == max_iterations:
                return

            x = X[i]
            y = Y[i]
            p_i = b0 + b1 * x
            error = p_i - y
            b0 = b0 - error * x * ALPHA
            b1 = b1 - error * ALPHA

            iteration += 1
            print("Iteration: %3d | erreur=%20f b0=%20f , b1=%20f" % \
            (iteration, error, b0, b1))
    
print("Gradient Descent with values: X={}, Y={}, ALPHA={}".format(X,Y,ALPHA))
gd(max_iterations=30)