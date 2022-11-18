import numpy as np

def simplex(s_t, v_j, v_i, n, m, x):
    count_iter = 0
    for j in range (1, n-1, 1):
        if s_t[m-2][j] > 0:
            pos = 1
    while pos:
        pos = 0
        count_iter += 1
        for j in range(1, n - 1, 1):
            if s_t[m-2][j] > 0:
                if v_j[j] > 0:
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
        index = v_j[resolve_j]
        v_j[resolve_j] = v_i[resolve_i]
        v_i[resolve_i] = index
        v_i[resolve_i+1] = index
        s_t = s_t_new
        for j in range(1, n - 1, 1):
            if v_j[j] > 0:
                if (not np.isclose(s_t[m-2][j], 0)) and np.sign(s_t[m-2][j]) > 0:
                    pos = 1
        print(s_t, "\n")
    x_array = np.zeros(x+1)
    x_array[0] = 1
    for i in range(0, m-2, 2):
        x_array[v_i[i]] = s_t[i][0]
    return x_array, count_iter, s_t, v_j, v_i


def classic_method():
    '''simplex_table = np.array([[1, -1, 1, 0],
                             [0, 0, 0, 0],
                             [2, 2, -1, 0],
                             [0, 0, 0, 0],
                             [7, 0, 2, 0],
                             [0, 0, 0, 0]], dtype='float')
    var_j = np.array([0, 3, 4, 0])
    var_i = np.array([1, 1, 2, 2, 0, 0])
    L_coeff = np.array([0, 5, 1, -3, 2])'''
    simplex_table = np.array([[8,4,1,2,1,0],
                              [0,0,0,0,0,0],
                              [2,2,-1,1,0,0],
                              [0,0,0,0,0,0],
                              [2,1,1,0,1,0],
                              [0,0,0,0,0,0],
                              [4,3,0,1,1,0],
                              [0,0,0,0,0,0]], dtype='float')
    var_j = np.array([0, 1, 2, 4, 5, 0])
    var_i = np.array([3, 3, -1, -1, 2, 2, 0, 0])
    L_coeff = np.array([0, 5, 1, -3, 2])
    print("Classic simplex method\n")
    print("Start table\n", simplex_table, "\n")
    x_array, count_iter, s_t, var_j, var_i = simplex(simplex_table, var_j, var_i, var_j.size, var_i.size, L_coeff.size-1)
    L = 0
    for i in range(1, x_array.size, 1):
        print("x", i, "=", x_array[i])
        L += L_coeff[i] * x_array[i]
    print("L_min =", L, "iteration =", count_iter, "\n------------------------------")


def v_method():
    simplex_table = np.array([[7, 3, 2, 1, 1, 0],
                             [0, 0, 0, 0, 0, 0],
                             [11, 5, 3, 1, 2, 0],
                             [0, 0, 0, 0, 0, 0],
                             [18, 8, 5, 2, 3, 0],
                             [0, 0, 0, 0, 0, 0]], dtype='float')
    var_j = np.array([0, 1, 2, 3, 4, 0])
    var_i = np.array([-1, -1, -2, -2, 0, 0])
    L_coeff = np.array([0, 5, 1, -3, 2])
    count_iter = 0
    print("V-method\n")
    print("Start table\n", simplex_table, "\n")
    x_array, iter, s_t, var_j, var_i = simplex(simplex_table, var_j, var_i, var_j.size, var_i.size, L_coeff.size-1)
    count_iter += iter
    for j in range (0, var_j.size, 1):
        if j == 0:
            for k in range(0, x_array.size, 1):
                s_t[var_i.size - 2][0] += L_coeff[k]*x_array[k]
        if var_j[j] > 0:
            s_t[var_i.size - 2][j] = L_coeff[var_j[j]]
            for i in range (0, var_i.size-2, 2):
                s_t[var_i.size-2][j] += L_coeff[var_i[i]]*(-s_t[i][j])
            s_t[var_i.size - 2][j] *= -1
    x_array, iter, s_t, var_j, var_i = simplex(s_t, var_j, var_i, var_j.size, var_i.size, L_coeff.size-1)
    count_iter += iter
    L = 0
    for i in range(1, x_array.size, 1):
        print("x", i, "=", x_array[i])
        L += L_coeff[i]*x_array[i]
    print("L_min =", L, "iteration =", count_iter, "\n------------------------------")

def m_method():
    M = 100
    simplex_table = np.array([[7, 3, 2, 1, 1, 0],
                             [0, 0, 0, 0, 0, 0],
                             [11, 5, 3, 1, 2, 0],
                             [0, 0, 0, 0, 0, 0],
                             [18*M, 8*M-5, 5*M-1, 2*M+3, 3*M-2, 0],
                             [0, 0, 0, 0, 0, 0]], dtype='float')
    var_j = np.array([0, 1, 2, 3, 4, 0])
    var_i = np.array([-1, -1, -2, -2, 0, 0])
    L_coeff = np.array([0, 5, 1, -3, 2])
    print("M-method\n")
    print("Start table\n", simplex_table, "\n")
    x_array, count_iter, s_t, var_j, var_i = simplex(simplex_table, var_j, var_i, var_j.size, var_i.size, L_coeff.size-1)
    L = 0
    for i in range(1, x_array.size, 1):
        print("x", i, "=", x_array[i])
        L += L_coeff[i] * x_array[i]
    print("L_min =", L, "iteration =", count_iter, "\n------------------------------")


if __name__ == "__main__":
    classic_method()
    v_method()
    m_method()



