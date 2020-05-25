import numpy as np
import matplotlib.pyplot as plt
from math import pow

# TODO: Generate a base method and inherit to eliminate duplication of code.
# TODO: Throw clean errors instead of print return

def linear(minmax, step=1, coef=0, noise=0):
    x = np.arange(minmax[0], minmax[1], step)
    delta = np.random.uniform(-noise, noise, minmax[1])
    y = coef * x + delta
    plt.plot(x,y)
    plt.show()
    return (x,y)

#TODO: Need to fix up negative
def quadratic(minmax, step=1, coef=0, noise=0):
    if len(coef) != 2:
        print("There must be equal number of coefficients to powers")
        return None
    x = np.arange(minmax[0], minmax[1], step)
    delta = np.random.uniform(-noise, noise, minmax[1]-minmax[0])
    y = coef[0] * x * x + coef[1] * x + delta
    print(x)
    print(y)
    plt.plot(x,y)
    plt.show()
    return (x,y)

def polynomial(minmax, step, power, coef, noise=0):
    if len(coef) != power:
        print("There must be equal number of coefficients to powers")
        return None
    x = np.arange(minmax[0], minmax[1], step)
    delta = np.random.uniform(-noise, noise, minmax[1])
    equation = [pow(x, i) for i in range(minmax[1], minmax[0], -step )]
    y = pow(x,power) + coef * x + delta
    plt.plot(x,y)
    plt.show()
    return (x,y)

def normal(minmax, step, coef, noise=0):
    # x = np.arange(minmax[1]-minmax[0])
    print("To Be Implemented")

def binomial(minmax, step, coef, noise=0):
    print("To Be Implemented")
    return None

