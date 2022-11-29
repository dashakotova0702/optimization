import numpy as np


def south_west_angle(a, b, m, n):
    x = np.zeros((m, n))
    for i in range(0, m, 1):
        for j in range(0, n, 1):
            x[i][j] = min(a[i], b[j])
            a[i] = a[i] - x[i][j]
            b[j] = b[j] - x[i][j]
    return x


def turn_up(p, l_i, l_j):
    i = l_i[len(l_i)-1]
    j = l_j[len(l_j)-1]
    count = 0
    while i != 0:
        count += 1
        i -= 1
        if p[i][j] > 0 or (i == l_i[0] and j == l_j[0]):
            break
    if i == l_i[0] and j == l_j[0] and len(l_i) > 1:
        return l_i, l_j
    if i == 0:
        if (i == l_i[0] and j == l_j[0] and len(l_i) == 1) or p[i][j] == 0:
            l_i.append(-1)
            l_j.append(-1)
            return l_i, l_j
        if p[i][j] > 0 and not count:
            l_i.append(-1)
            l_j.append(-1)
            return l_i, l_j
    if p[i][j] > 0:
        l_i.append(i)
        l_j.append(j)
        l_i, l_j = turn_left(p, l_i, l_j)
        if l_i[len(l_i)-1] < 0 and l_j[len(l_j)-1] < 0:
            l_i.pop()
            l_j.pop()
            l_i, l_j = turn_right(p, l_i, l_j)
            if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
                l_i.pop()
                l_j.pop()
                if l_i[len(l_i) - 1] != 0:
                    l_i, l_j = turn_up(p, l_i, l_j)
                    if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
                        l_i.pop()
                        l_j.pop()
                        l_i.pop()
                        l_j.pop()
                        l_i.append(-1)
                        l_j.append(-1)
                else:
                    l_i.pop()
                    l_j.pop()
                    l_i.append(-1)
                    l_j.append(-1)
        return l_i, l_j


def turn_left(p, l_i, l_j):
    i = l_i[len(l_i) - 1]
    j = l_j[len(l_j) - 1]
    count = 0
    while j != 0:
        count += 1
        j -= 1
        if p[i][j] > 0 or (i == l_i[0] and j == l_j[0]):
            break
    if i == l_i[0] and j == l_j[0] and len(l_i) > 1:
        return l_i, l_j
    if j == 0:
        if (i == l_i[0] and j == l_j[0] and len(l_i) == 1) or p[i][j] == 0:
            l_i.append(-1)
            l_j.append(-1)
            return l_i, l_j
        if p[i][j] > 0 and not count:
            l_i.append(-1)
            l_j.append(-1)
            return l_i, l_j
    if p[i][j] > 0:
        l_i.append(i)
        l_j.append(j)
        l_i, l_j = turn_up(p, l_i, l_j)
        if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
            l_i.pop()
            l_j.pop()
            l_i, l_j = turn_down(p, l_i, l_j)
            if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
                l_i.pop()
                l_j.pop()
                if l_j[len(l_j)-1] != 0:
                    l_i, l_j = turn_left(p, l_i, l_j)
                    if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
                        l_i.pop()
                        l_j.pop()
                        l_i.pop()
                        l_j.pop()
                        l_i.append(-1)
                        l_j.append(-1)
                else:
                    l_i.pop()
                    l_j.pop()
                    l_i.append(-1)
                    l_j.append(-1)
        return l_i, l_j


def turn_down(p, l_i, l_j):
    i = l_i[len(l_i) - 1]
    j = l_j[len(l_j) - 1]
    count = 0
    while i != p.shape[0]-1:
        count += 1
        i += 1
        if p[i][j] > 0 or (i == l_i[0] and j == l_j[0]):
            break
    if i == l_i[0] and j == l_j[0] and len(l_i) > 1:
        return l_i, l_j
    if i == p.shape[0]-1:
        if (i == l_i[0] and j == l_j[0] and len(l_i) == 1) or p[i][j] == 0:
            l_i.append(-1)
            l_j.append(-1)
            return l_i, l_j
        if p[i][j] > 0 and not count:
            l_i.append(-1)
            l_j.append(-1)
            return l_i, l_j
    if p[i][j] > 0:
        l_i.append(i)
        l_j.append(j)
        l_i, l_j = turn_left(p, l_i, l_j)
        if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
            l_i.pop()
            l_j.pop()
            l_i, l_j = turn_right(p, l_i, l_j)
            if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
                l_i.pop()
                l_j.pop()
                if l_i[len(l_i) - 1] != p.shape[0]-1:
                    l_i, l_j = turn_down(p, l_i, l_j)
                    if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
                        l_i.pop()
                        l_j.pop()
                        l_i.pop()
                        l_j.pop()
                        l_i.append(-1)
                        l_j.append(-1)
                else:
                    l_i.pop()
                    l_j.pop()
                    l_i.append(-1)
                    l_j.append(-1)
        return l_i, l_j


def turn_right(p, l_i, l_j):
    i = l_i[len(l_i) - 1]
    j = l_j[len(l_j) - 1]
    count = 0
    while j != p.shape[1] - 1:
        count += 1
        j += 1
        if p[i][j] > 0 or (i == l_i[0] and j == l_j[0]):
            break
    if i == l_i[0] and j == l_j[0] and len(l_i) > 1:
        return l_i, l_j
    if j == p.shape[1] - 1:
        if (i == l_i[0] and j == l_j[0] and len(l_i) == 1) or p[i][j] == 0:
            l_i.append(-1)
            l_j.append(-1)
            return l_i, l_j
        if p[i][j] > 0 and not count:
            l_i.append(-1)
            l_j.append(-1)
            return l_i, l_j
    if p[i][j] > 0:
        l_i.append(i)
        l_j.append(j)
        l_i, l_j = turn_up(p, l_i, l_j)
        if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
            l_i.pop()
            l_j.pop()
            l_i, l_j = turn_down(p, l_i, l_j)
            if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
                l_i.pop()
                l_j.pop()
                if l_j[len(l_j) - 1] != p.shape[1] - 1:
                    l_i, l_j = turn_right(p, l_i, l_j)
                    if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
                        l_i.pop()
                        l_j.pop()
                        l_i.pop()
                        l_j.pop()
                        l_i.append(-1)
                        l_j.append(-1)
                else:
                    l_i.pop()
                    l_j.pop()
                    l_i.append(-1)
                    l_j.append(-1)
        return l_i, l_j


def labirint(p, list_i, list_j):
    l_i, l_j = turn_up(p, list_i, list_j)
    if l_i[len(l_i)-1] < 0 and l_j[len(l_j)-1] < 0:
        l_i.pop()
        l_j.pop()
        l_i, l_j = turn_left(p, list_i, list_j)
        if l_i[len(l_i)-1] < 0 and l_j[len(l_j)-1] < 0:
            l_i.pop()
            l_j.pop()
            l_i, l_j = turn_down(p, list_i, list_j)
            if l_i[len(l_i)-1] < 0 and l_j[len(l_j)-1] < 0:
                l_i.pop()
                l_j.pop()
                l_i, l_j = turn_right(p, list_i, list_j)
    return l_i, l_j


def potentional_method(plan, t, m, n):
    while True:
        C = 0
        for i in range(0, m, 1):
            for j in range(0, n, 1):
                if plan[i][j] > 0:
                    C += t[i][j]*np.round(plan[i][j], 9)
        print("Стоимость перевозок по данному плану:", C)
        alpha = np.zeros(m)
        beta = np.zeros(n)
        zero = 0
        for i in range(0, m, 1):
            for j in range(0, n, 1):
                for k in range(0, m, 1):
                    if k != i:
                        if plan[k][j] > 0:
                            zero += 1
                for l in range(0, n, 1):
                    if l != j:
                        if plan[i][l] > 0:
                            zero += 1
                if zero > 0:
                    zero = 0
                else:
                    for k in range(0, m, 1):
                        if k != i:
                            if plan[k][j] == 0:
                                plan[k][j] = 10**(-10)
                                break
        not_zero_elem = 0
        for i in range(0, m, 1):
            for j in range(0, n, 1):
                if plan[i][j] > 0:
                    not_zero_elem += 1
        if not_zero_elem < m+n-1:
            if plan[0][0] == 0:
                plan[0][0] = 10**(-10)
            elif plan[0][plan.shape[1]-1] == 0:
                plan[0][plan.shape[1] - 1] = 10**(-10)
        matrix = np.zeros((m+n, m+n))
        free = np.zeros(m+n)
        matrix[0][0] = 1
        matrix_c = 1
        for i in range(0, m, 1):
            for j in range(0, n, 1):
                if plan[i][j]:
                    matrix[matrix_c][i] = 1
                    matrix[matrix_c][j+m] = 1
                    free[matrix_c] = t[i][j]
                    matrix_c += 1
        alpha_beta = np.linalg.solve(matrix, free)
        for i in range(0, m, 1):
            alpha[i] = alpha_beta[i]
        for i in range(m, m+n, 1):
            beta[i-m] = alpha_beta[i]
        exit = 0
        for i in range(0, m, 1):
            for j in range(0, n, 1):
                if plan[i][j] == 0:
                    if alpha[i] + beta[j] > t[i][j]:
                        exit += 1
                        if exit == 1:
                            i_ = i
                            j_ = j
        if not exit:
            return plan
        else:
            list_index_i = []
            list_index_j = []
            list_index_i.append(i_)
            list_index_j.append(j_)
            list_index_i, list_index_j = labirint(plan, list_index_i, list_index_j)
            index_delete = []
            for k in range(1, len(list_index_i)-1, 1):
                if (list_index_i[k-1] == list_index_i[k] and list_index_i[k] == list_index_i[k+1]) or \
                        (list_index_j[k] == list_index_j[k - 1] and list_index_j[k] == list_index_j[k + 1]):
                    index_delete.append(k)
            if (list_index_i[len(list_index_i)-2] == list_index_i[len(list_index_i)-1] and \
                    list_index_i[len(list_index_i)-1] == list_index_i[0]) or \
                    (list_index_j[len(list_index_j)-2] == list_index_j[len(list_index_j)-1] and \
                     list_index_j[len(list_index_i)-1] == list_index_j[0]):
                index_delete.append(len(list_index_i)-1)
            list_index_i = np.delete(list_index_i, index_delete)
            list_index_j = np.delete(list_index_j, index_delete)
            min_elem = []
            for k in range(1, len(list_index_j), 2):
                min_elem.append(plan[list_index_i[k]][list_index_j[k]])
            min_elem = min(min_elem)
            for k in range(0, len(list_index_j), 2):
                plan[list_index_i[k]][list_index_j[k]] += min_elem
            for k in range(1, len(list_index_j), 2):
                plan[list_index_i[k]][list_index_j[k]] -= min_elem
            print("--------------------------------------------------------\n\n")
            print("Опорный план:\n", plan)


if __name__ == "__main__":
    table = np.array([[18, 20, 14, 10],
                      [10, 20, 40, 30],
                      [16, 22, 10, 20]])
    table_a = np.array([90, 30, 40])
    table_b = np.array([70, 30, 20, 40])
    '''table = np.array([[4, 1, 8, 3],
                      [5, 7, 0, 9],
                      [7, 1, 3, 2]])
    table_a = np.array([50, 190, 110])
    table_b = np.array([70, 30, 150, 100])'''
    '''table = np.array([[7, 1, 4, 6, 5, 8],
                      [1, 3, 5, 2, 4, 6],
                      [4, 5, 6, 3, 1, 7],
                      [5, 3, 7, 2, 8, 4],
                      [2, 4, 3, 5, 6, 3]])
    table_a = np.array([600, 800, 550, 730, 900])
    table_b = np.array([750, 580, 440, 620, 550, 640])'''
    count_factory = 3
    count_client = 4
    '''count_factory = 5
    count_client = 6'''
    print("Количество заводов:", count_factory)
    print("Количество клиентов:", count_client)
    print("Стоимости перевозок:\n", table)
    print("Количество товара на заводах:\n", table_a)
    print("Необходимо поставить клиентам:\n", table_b)
    plan = south_west_angle(table_a, table_b, count_factory, count_client)
    print("Начальный опорный план:\n", plan)
    plan = potentional_method(plan, table, count_factory, count_client)