import numpy as np
import matplotlib.pyplot as plt
from sympy import *

def parabola_method(func):
    x, z = symbols("x, z")
    x_1 = -1
    x_2 = -0.9
    x_3 = -0.5
    func_x_1 = func.subs(x, x_1)
    func_x_2 = func.subs(x, x_2)
    func_x_3 = func.subs(x, x_3)
    delta = 1000
    x_min_back = 1000
    eps = 0.01
    count = 0
    while abs(delta) >= eps:
        a_1 = (func_x_2-func_x_1)/(x_2-x_1)
        a_2 = (1/(x_3-x_2))*((func_x_3-func_x_1)/(x_3-x_1)-(func_x_2-func_x_1)/(x_2-x_1))
        x_min_now = (x_1+x_2-a_1/a_2)/2
        func_x_min = func.subs(x, x_min_now)
        if x_min_now < x_2:
            if func_x_2 < func_x_min:
                x_1 = x_min_now
                func_x_1 = func_x_min
            if func_x_2 >= func_x_min:
                x_3 = x_2
                func_x_3 = func_x_2
                x_2 = x_min_now
                func_x_2 = func_x_min
        if x_min_now > x_2:
            if func_x_2 <= func_x_min:
                x_3 = x_min_now
                func_x_3 = func_x_min
            if func_x_2 > func_x_min:
                x_1 = x_2
                func_x_1 = func_x_2
                x_2 = x_min_now
                func_x_2 = func_x_min
        delta = x_min_now - x_min_back
        x_min_back = x_min_now
        count += 1
    plt.title('Метод парабол')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    x_array = np.arange(-1, 2.01, 0.01)
    func_array = np.zeros(x_array.size)
    for i in range(0, x_array.size, 1):
        func_array[i] = func.subs(x, x_array[i])
    plt.plot(x_array, func_array, color='b', label='f(x)')
    plt.plot(x_min_back, func_x_min, 'ro', label='min')
    plt.legend()
    plt.figure()
    return x_min_back, func_x_min, count


def midpoint_method(func):
    x = symbols("x")
    a = -1
    b = 2
    x_min = (a+b)/2
    func_diff = func.diff(x)
    func_diff_x_min = func_diff.subs(x, x_min)
    eps = 0.01
    count = 0
    while abs(func_diff_x_min) >= eps:
        if func_diff_x_min < 0:
            a = x_min
        if func_diff_x_min > 0:
            b = x_min
        x_min = (a+b)/2
        func_diff_x_min = func_diff.subs(x, x_min)
        count += 1
    func_x_min = func.subs(x, x_min)
    plt.title('Метод средней точки')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    x_array = np.arange(-1, 2.01, 0.01)
    func_array = np.zeros(x_array.size)
    for i in range(0, x_array.size, 1):
        func_array[i] = func.subs(x, x_array[i])
    plt.plot(x_array, func_array, color='b', label='f(x)')
    plt.plot(x_min, func_x_min, 'ro', label='min')
    plt.legend()
    plt.figure()
    return x_min, func_x_min, count


def chord_method(func):
    x = symbols("x")
    a = -0.99
    b = 2
    func_diff = func.diff(x)
    func_diff_a = func_diff.subs(x, a)
    func_diff_b = func_diff.subs(x, b)
    x_min = a - func_diff_a*(a-b)/(func_diff_a-func_diff_b)
    func_diff_x_min = func_diff.subs(x, x_min)
    eps = 0.01
    count = 0
    while abs(func_diff_x_min) >= eps:
        if func_diff_x_min < 0:
            a = x_min
            func_diff_a = func_diff_x_min
        if func_diff_x_min > 0:
            b = x_min
            func_diff_b = func_diff_x_min
        x_min = a - func_diff_a * (a - b) / (func_diff_a - func_diff_b)
        func_diff_x_min = func_diff.subs(x, x_min)
        count += 1
    func_x_min = func.subs(x, x_min)
    plt.title('Метод хорд')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    x_array = np.arange(-0.99, 2.01, 0.01)
    func_array = np.zeros(x_array.size)
    func_diff_array = np.zeros(x_array.size)
    for i in range(0, x_array.size, 1):
        func_array[i] = func.subs(x, x_array[i])
        func_diff_array[i] = func_diff.subs(x, x_array[i])
    plt.plot(x_array, func_array, color='b', label='f(x)')
    plt.plot(x_array, func_diff_array, color='g', label='f\'(x)')
    plt.plot(x_min, func_x_min, 'ro', label='min')
    plt.legend()
    plt.figure()
    return x_min, func_x_min, count


if __name__ == "__main__":
    x = symbols("x")
    func = x * pow((pow(x, 3)+1), 0.5)-pow(x, 2)
    print('                             x_min               f(x)_min    iteration')
    print('Метод парабол:           ', parabola_method(func))
    print('Метод средней точки:', midpoint_method(func))
    print('Метод хорд:', chord_method(func))
    plt.show()