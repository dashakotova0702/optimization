import sympy as sp
import numpy as np

def simplex(s_t, v_j, v_i, n, m):
    count_iter = 0
    for j in range (1, n-1, 1):
        if s_t[m-1][j] >= 0:
            pos = 1
    while pos:
        pos = 0
        count_iter += 1
        for j in range(1, n - 1, 1):
            if s_t[m-2][j] >= 0:
                if v_j[j] >= 0:
                    resolve_j = j
                    break
        min_a_b = 1000000
        for i in range(0, m-2, 2):
            if s_t[i][resolve_j] > 0:
                s_t[i][n-1] = s_t[i][0]/s_t[i][resolve_j]
                if s_t[i][n-1] < min_a_b:
                    min_a_b = s_t[i][n-1]
                    resolve_i = i
        lmbd = 1/s_t[resolve_i][resolve_j]
        s_t[resolve_i+1][resolve_j] = lmbd
        for j in range(0, n-1, 1):
            if j != resolve_j:
                s_t[resolve_i+1][j] = s_t[resolve_i][j]*lmbd
        for i in range(1, m, 2):
            if i != resolve_i+1:
                s_t[i][resolve_j] = s_t[i-1][resolve_j]*(-lmbd)
        for i in range (1, m, 2):
            for j in range (0, n-1, 1):
                if i != resolve_i+1 and j != resolve_j:
                    s_t[i][j] = s_t[i][resolve_j]*s_t[resolve_i][j]
        s_t_new = np.zeros((m, n))
        for i in range(0, m, 2):
            for j in range(0, n - 1, 1):
                if i != resolve_i and j != resolve_j:
                    s_t_new[i][j] = s_t[i][j] + s_t[i+1][j]
                else:
                    s_t_new[i][j] = s_t[i+1][j]
        if v_i[resolve_i] < 0:
            index = v_j[resolve_j]
            v_j[resolve_j] = v_i[resolve_i]
            v_i[resolve_i] = index
            v_i[resolve_i+1] = index
        s_t = s_t_new
        for j in range(1, n - 1, 1):
            if s_t[m-1][j] >= 0:
                pos = 1
        print(s_t)
    print("L_min= ", s_t[m-1][0], "iteration= ", count_iter)
    for i in range(0, m-2, 2):
        print("x", v_i[i], "= ", s_t[i][0])
    for j in range(0, n-1, 1):
        print("x", v_j[j], "= 0")


def classic_simplex():
    simplex_table = np.array([[1, -1, 1, 0],
                             [0, 0, 0, 0],
                             [2, 2, -1, 0],
                             [0, 0, 0, 0],
                             [7, 0, -2, 0],
                             [0, 0, 0, 0]], dtype='float')
    var_j = np.array([0, 3, 4, 0])
    var_i = np.array([1, 1, 2, 2, 0, 0])
    simplex(simplex_table, var_j, var_i, 4, 6)


def v_method():
    simplex_table = np.array([[7, 3, 2, 1, 1, 0],
                             [0, 0, 0, 0, 0, 0],
                             [11, 5, 3, 1, 2, 0],
                             [0, 0, 0, 0, 0, 0],
                             [18, 8, 5, 2, 3, 0],
                             [0, 0, 0, 0, 0, 0]], dtype='float')
    var_j = np.array([0, 1, 2, 3, 4, 0])
    var_i = np.array([-1, -1, -2, -2, 0, 0])
    simplex(simplex_table, var_j, var_i, 6, 6)

if __name__ == "__main__":
    v_method()



