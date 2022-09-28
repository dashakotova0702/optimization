import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols


def dichotomy_method(func):



def golden_ratio(func):



if __name__ == "__main__":
    x = symbols("x")
    func = x * pow((pow(x, 3)+1), 0.5)-pow(x, 2)
    print('                             x_min               f(x)_min    iteration')
    print('Метод дихотомии:           ', dichotomy_method(func))
    print('Метод золотого сечения:', golden_ratio(func))
    plt.show()