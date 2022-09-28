import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols


def dichotomy_method(func):
    x = symbols('x')
    a = -1
    b = 2
    eps = 0.01
    eps_n = 1
    delta = eps/2
    count = 0
    while eps_n > eps:
        count += 1
        x_1 = (a + b) / 2 - delta
        x_2 = (a + b) / 2 + delta
        func_x_1 = func.subs(x, x_1)
        func_x_2 = func.subs(x, x_2)
        if func_x_1 > func_x_2:
            a = x_1
        if func_x_1 < func_x_2:
            b = x_2
        eps_n = (b - a) / 2
    x_min = (a+b)/2
    func_x_min = func.subs(x, x_min)
    x_array = np.arange(-1, 2.01, 0.01)
    func_array = np.zeros(x_array.size)
    for i in range(0, x_array.size, 1):
        func_array[i] = func.subs(x, x_array[i])
    plt.title('Метод дихотомии')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(x_array, func_array, color='b', label='f(x)')
    plt.plot(x_min, func_x_min, 'ro', label='min')
    plt.legend()
    plt.figure()
    return x_min, func_x_min, count


def golden_ratio(func):
    x = symbols('x')
    a = -1
    b = 2
    eps = 0.01
    eps_n = (b - a) / 2
    count = 0
    x_1 = b - (b - a) * (np.sqrt(5) - 1) / 2
    x_2 = a + (b - a) * (np.sqrt(5) - 1) / 2
    func_x_1 = func.subs(x, x_1)
    func_x_2 = func.subs(x, x_2)
    while eps_n > eps:
        count += 1
        if func_x_1 > func_x_2:
            a = x_1
            x_1 = x_2
            func_x_1 = func_x_2
            x_2 = a + (b - a) * (np.sqrt(5) - 1) / 2
            func_x_2 = func.subs(x, x_2)
        if func_x_1 < func_x_2:
            b = x_2
            x_2 = x_1
            func_x_2 = func_x_1
            x_1 = b - (b - a) * (np.sqrt(5) - 1) / 2
            func_x_1 = func.subs(x, x_1)
        eps_n = (b - a) / 2
    x_min = (a + b) / 2
    func_x_min = func.subs(x, x_min)
    x_array = np.arange(-1, 2.01, 0.01)
    func_array = np.zeros(x_array.size)
    for i in range(0, x_array.size, 1):
        func_array[i] = func.subs(x, x_array[i])
    plt.title('Метод золотого сечения')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(x_array, func_array, color='b', label='f(x)')
    plt.plot(x_min, func_x_min, 'ro', label='min')
    plt.legend()
    return x_min, func_x_min, count



if __name__ == "__main__":
    x = symbols("x")
    func = x * pow((pow(x, 3)+1), 0.5)-pow(x, 2)
    print('                             x_min               f(x)_min    iteration')
    print('Метод дихотомии:           ', dichotomy_method(func))
    print('Метод золотого сечения:    ', golden_ratio(func))
    plt.show()