import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols


def brute_force_method(func):
    x = symbols('x')
    x_array = np.arange(-1, 2.01, 0.01)
    func_array = np.zeros(x_array.size)
    index = 0
    for i in range(0, x_array.size, 1):
        func_array[i] = func.subs(x, x_array[i])
    func_min = min(func_array)
    for i in func_array:
        index += 1
        if i == func_min:
            break
    x_min = x_array[index]
    plt.title('Метод перебора')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(x_array, func_array, color='b', label='f(x)')
    plt.plot(x_min, func_min, 'ro', label='min')
    plt.legend()
    plt.figure()
    return x_min, func_min, x_array.size


def bitwise_search_method(func):
    x = symbols('x')
    x_now = -1
    eps = 0.01
    count, count_iter, count_step = 0, 0, 0
    eps_step = -(2+1)
    func_back, func_now = 100, 0
    x_min, func_min = 0, 0
    while abs(eps_step) > eps:
        eps_step = -eps_step/4
        while func_back > func_now or count_iter == 0:
            count += 1
            count_iter += 1
            if count_iter == 1:
                func_back = func.subs(x, x_now)
                x_now += eps_step
                func_now = func.subs(x, x_now)
            else:
                func_back = func_now
                x_now += eps_step
                func_now = func.subs(x, x_now)
        count_iter = 0
        count_step += 1
        x_min = x_now - eps_step
        func_min = func_back
    x_array = np.arange(-1, 2.01, 0.01)
    func_array = np.zeros(x_array.size)
    for i in range(0, x_array.size, 1):
        func_array[i] = func.subs(x, x_array[i])
    plt.title('Метод поразрядного поиска')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.plot(x_array, func_array, color='b', label='f(x)')
    plt.plot(x_min, func_min, 'ro', label='min')
    plt.legend()
    return x_min, func_min, count


if __name__ == "__main__":
    x = symbols("x")
    func = x * pow((pow(x, 3)+1), 0.5)-pow(x, 2)
    print('                             x_min               f(x)_min    iteration')
    print('Метод перебора:           ', brute_force_method(func))
    print('Метод поразрядного поиска:', bitwise_search_method(func))
    plt.show()