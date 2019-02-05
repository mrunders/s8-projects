# -*- coding: utf-8 -*-

from sys import argv
from matplotlib import pyplot as plt
from math import exp

sigmoid = lambda x : 1 / (1 + exp(-x))
sigmoid_deriv = lambda x : x * (1 - x)

vals = int(argv[1])
xrang = range(-vals, vals)

plt.plot(xrang, map(sigmoid, xrang), "b", linewidth=0.8, marker="*")
plt.plot(xrang, map(sigmoid_deriv, xrang), "g", linewidth=0.8, marker="+")
plt.ylabel('Sigmoid')
plt.show()