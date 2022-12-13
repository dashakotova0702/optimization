import numpy as np
from lab6_choise import *


def hungarian_method_transp(t, t_i, t_j, m, n):
    c_0 = np.array(t)
    for j in range(0, m, 1):
        min_j = min(c_0[:, j])
        for i in range(0, n, 1):
            c_0[i][j] -= min_j
    for i in range(0, n, 1):
        min_i = min(c_0[i])
        for j in range(0, n, 1):
            c_0[i][j] -= min_i
    x = np.zeros((n, m))
    nev_i = np.array(t_i)
    nev_j = np.array(t_j)
    for j in range(0, m, 1):
        for i in range(0, n, 1):
            if c_0[i][j] == 0:
                x[i][j] = min([nev_i[i], nev_j[j]])
                nev_i[i] -= x[i][j]
                nev_j[j] -= x[i][j]
    print("--------------------------------------------------------\n")
    print("Опорный план:\n", x)
    notes = np.chararray((n, m))
    notes[:] = '-'
    plus_i = np.chararray(n)
    plus_i[:] = '-'
    plus_j = np.chararray(m)
    plus_j[:] = '-'
    while True:
        nev_i = np.zeros(n)
        nev_j = np.zeros(m)
        delta = 0
        for j in range(0, m, 1):
            sum = 0
            for i in range(0, n, 1):
                sum += x[i][j]
            nev_j[j] = t_j[j] - sum
            delta += nev_j[j]
        for i in range(0, n, 1):
            sum = 0
            for j in range(0, m, 1):
                sum += x[i][j]
            nev_i[i] = t_i[i] - sum
            delta += nev_i[i]
        if delta == 0:
            return x
        else:
            for j in range(0, m, 1):
                if nev_j[j] == 0:
                    plus_j[j] = '+'
            not_mark_zero = 0
            for i in range(0, n, 1):
                for j in range(0, m, 1):
                    if not not_mark_zero and c_0[i][j] == 0 and notes[i][j] == b'-' \
                            and plus_i[i] == b'-' and plus_j[j] == b'-':
                        not_mark_zero = 1
                        index_i_not_mark_zero = i
                        index_j_not_mark_zero = j
            if not_mark_zero:
                if nev_i[index_i_not_mark_zero] == 0:
                    plus_i[index_i_not_mark_zero] = '+'
                    notes[index_i_not_mark_zero][index_j_not_mark_zero] = b'|'
                    for j in range(0, m, 1):
                        if plus_j[j] == b'+':
                            if x[index_i_not_mark_zero][j] > 0:
                                notes[index_i_not_mark_zero][j] = '*'
                else:
                    notes[index_i_not_mark_zero][index_j_not_mark_zero] = b'|'
                    list_index_i = []
                    list_index_j = []
                    list_index_i.append(index_i_not_mark_zero)
                    list_index_j.append(index_j_not_mark_zero)
                    list_index_i, list_index_j = labirint(notes, list_index_i, list_index_j)
                    min_elem_chain = 10000
                    if len(list_index_j) > 1:
                        for k in range(1, len(list_index_i), 2):
                            if x[list_index_i[k]][list_index_j[k]] < min_elem_chain:
                                min_elem_chain = x[list_index_i[k]][list_index_j[k]]
                    if nev_i[list_index_i[0]] < min_elem_chain:
                        min_elem_chain = nev_i[list_index_i[0]]
                    if nev_j[list_index_j[len(list_index_j)-1]] < min_elem_chain:
                        min_elem_chain = nev_j[list_index_j[len(list_index_j)-1]]
                    if len(list_index_j) > 1:
                        for k in range(1, len(list_index_i), 2):
                            x[list_index_i[k]][list_index_j[k]] -= min_elem_chain
                    for k in range(0, len(list_index_i), 2):
                        x[list_index_i[k]][list_index_j[k]] += min_elem_chain
                    print("\n---------------------------------------\n\n")
                    print("План:\n", x)
                    print("\nC:\n", c_0)
                    print(notes)
                    notes[:] = '-'
                    plus_i[:] = '-'
                    plus_j[:] = '-'
            else:
                min_not_mark_elem = 10000
                for j in range(0, m, 1):
                    for i in range(0, n, 1):
                        if plus_i[i] != b'+' and plus_j[j] != b'+':
                            if c_0[i][j] < min_not_mark_elem:
                                min_not_mark_elem = c_0[i][j]
                for j in range(0, m, 1):
                    if plus_j[j] == b'+':
                        for i in range(0, n, 1):
                            c_0[i][j] += min_not_mark_elem
                for i in range(0, n, 1):
                    if plus_i[i] != b'+':
                        for j in range(0, m, 1):
                            c_0[i][j] -= min_not_mark_elem
                print("\n---------------------------------------\n\n")
                print("План:\n", x)
                print("\nC:\n", c_0)
                print(notes)


if __name__ == "__main__":
    table = np.array([[18, 20, 14, 10],
                      [10, 20, 40, 30],
                      [16, 22, 10, 20]])
    table_a = np.array([90, 30, 40])
    table_b = np.array([70, 30, 20, 40])
    count_factory = 3
    count_client = 4
    print("Количество заводов:", count_factory)
    print("Количество клиентов:", count_client)
    print("Стоимости перевозок:\n", table)
    print("Количество товара на заводах:\n", table_a)
    print("Необходимо поставить клиентам:\n", table_b)
    plan = hungarian_method_transp(table, table_a, table_b, count_client, count_factory)
    print("----------------------------------------------\n\n")
    print("Оптимальный план перевозок:\n", plan)
    C = 0
    for i in range(0, count_factory, 1):
        for j in range(0, count_client, 1):
            if plan[i][j] > 0:
                C += table[i][j] * plan[i][j]
    print("\nСтоимость перевозок по данному плану:", C)