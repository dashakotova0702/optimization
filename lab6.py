import numpy as np


def turn_up(note, l_i, l_j):
    i = l_i[len(l_i) - 1]
    j = l_j[len(l_j) - 1]
    count = 0
    while i != 0:
        count += 1
        i -= 1
        if note[i][j] == b'*' or (i == l_i[0] and j == l_j[0]):
            break
    if i == 0:
        if (i == l_i[0] and j == l_j[0] and len(l_i) == 1) or note[i][j] != b'*':
            l_i.append(-1)
            l_j.append(-1)
            return l_i, l_j
    if note[i][j] == b'*':
        l_i.append(i)
        l_j.append(j)
        l_i, l_j = turn_left(note, l_i, l_j)
        if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
            l_i.pop()
            l_j.pop()
            l_i, l_j = turn_right(note, l_i, l_j)
        return l_i, l_j


def turn_left(note, l_i, l_j):
    i = l_i[len(l_i) - 1]
    j = l_j[len(l_j) - 1]
    count = 0
    while j != 0:
        count += 1
        j -= 1
        if note[i][j] == b'|' or (i == l_i[0] and j == l_j[0]):
            break
    if j == 0:
        if (i == l_i[0] and j == l_j[0] and len(l_i) == 1) or note[i][j] != b'|':
            l_i.append(-1)
            l_j.append(-1)
            return l_i, l_j
    if note[i][j] == b'|':
        l_i.append(i)
        l_j.append(j)
        l_i, l_j = turn_up(note, l_i, l_j)
        if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
            l_i.pop()
            l_j.pop()
            l_i, l_j = turn_down(note, l_i, l_j)
            if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
                l_i.pop()
                l_j.pop()
        return l_i, l_j


def turn_down(note, l_i, l_j):
    i = l_i[len(l_i) - 1]
    j = l_j[len(l_j) - 1]
    count = 0
    while i != note.shape[0] - 1:
        count += 1
        i += 1
        if note[i][j] == b'*' or (i == l_i[0] and j == l_j[0]):
            break
    if i == note.shape[0] - 1:
        if (i == l_i[0] and j == l_j[0] and len(l_i) == 1) or note[i][j] != b'*':
            l_i.append(-1)
            l_j.append(-1)
            return l_i, l_j
    if note[i][j] == b'*':
        l_i.append(i)
        l_j.append(j)
        l_i, l_j = turn_left(note, l_i, l_j)
        if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
            l_i.pop()
            l_j.pop()
            l_i, l_j = turn_right(note, l_i, l_j)
        return l_i, l_j


def turn_right(note, l_i, l_j):
    i = l_i[len(l_i) - 1]
    j = l_j[len(l_j) - 1]
    count = 0
    while j != note.shape[1] - 1:
        count += 1
        j += 1
        if note[i][j] == b'|' or (i == l_i[0] and j == l_j[0]):
            break
    if j == note.shape[1] - 1:
        if (i == l_i[0] and j == l_j[0] and len(l_i) == 1) or note[i][j] != b'|':
            l_i.append(-1)
            l_j.append(-1)
            return l_i, l_j
    if note[i][j] == b'|':
        l_i.append(i)
        l_j.append(j)
        l_i, l_j = turn_up(note, l_i, l_j)
        if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
            l_i.pop()
            l_j.pop()
            l_i, l_j = turn_down(note, l_i, l_j)
            if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
                l_i.pop()
                l_j.pop()
        return l_i, l_j


def labirint(note, list_i, list_j):
    l_i, l_j = turn_up(note, list_i, list_j)
    if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
        l_i.pop()
        l_j.pop()
        l_i, l_j = turn_down(note, list_i, list_j)
        if l_i[len(l_i) - 1] < 0 and l_j[len(l_j) - 1] < 0:
            l_i.pop()
            l_j.pop()
    return l_i, l_j


def hungarian_method(table):
    n = table.shape[0]
    m = table.shape[1]
    c_0 = np.array(table)
    for j in range(0, m, 1):
        max_j = max(c_0[:, j])
        for i in range(0, n, 1):
            c_0[i][j] = max_j - c_0[i][j]
    for i in range(0, n, 1):
        min_i = min(c_0[i])
        for j in range(0, n, 1):
            c_0[i][j] -= min_i
    notes = np.chararray((n, m))
    notes[:] = '-'
    plus_i = np.chararray(n)
    plus_i[:] = '-'
    plus_j = np.chararray(m)
    plus_j[:] = '-'
    for j in range(0, m, 1):
        q = 0
        for i in range(0, n, 1):
            if c_0[i][j] == 0 and notes[i][j] != b'*' and not q:
                star = 0
                for k in range(0, m, 1):
                    if c_0[i][k] == 0 and k != j and notes[i][k] == b'*':
                        star = 1
                if not star:
                    notes[i][j] = '*'
                    q = 1
    for j in range(0, m, 1):
        for i in range(0, n, 1):
            if notes[i][j] == b'*':
                plus_j[j] = '+'
    print("---------------------------------------\n\n")
    print("C:\n", c_0)
    print(notes)
    print("---------------------------------------\n\n")
    while True:
        not_mark_zero = 0
        for i in range(0, n, 1):
            for j in range(0, m, 1):
                if not not_mark_zero and c_0[i][j] == 0 and notes[i][j] == b'-' \
                        and plus_i[i] == b'-' and plus_j[j] == b'-':
                    not_mark_zero = 1
                    index_i_not_mark_zero = i
                    index_j_not_mark_zero = j
        if not_mark_zero:
            star = 0
            for j in range(0, m, 1):
                if notes[index_i_not_mark_zero][j] == b'*':
                    star_j = j
                    star = 1
            if star:
                notes[index_i_not_mark_zero][index_j_not_mark_zero] = '|'
                plus_i[index_i_not_mark_zero] = '+'
                plus_j[star_j] = '-'
            else:
                list_index_i = []
                list_index_j = []
                list_index_i.append(index_i_not_mark_zero)
                list_index_j.append(index_j_not_mark_zero)
                list_index_i, list_index_j = labirint(notes, list_index_i, list_index_j)
                for k in range(0, len(list_index_i), 1):
                    if notes[list_index_i[k]][list_index_j[k]] == b'*':
                        notes[list_index_i[k]][list_index_j[k]] = b'-'
                    else:
                        notes[list_index_i[k]][list_index_j[k]] = b'*'
                for i in range(0, n, 1):
                    for j in range(0, m, 1):
                        if notes[i][j] == b'|':
                            notes[i][j] = b'-'
                print("C:\n", c_0)
                print(notes)
                print("---------------------------------------\n\n")
                list_i = []
                list_j = []
                for i in range(0, n, 1):
                    for j in range(0, m, 1):
                        if notes[i][j] == b'*':
                            list_i.append(i)
                            list_j.append(j)
                if len(list_i) == n:
                    return list_i, list_j
                else:
                    plus_i[:] = '-'
                    plus_j[:] = '-'
                    for j in range(0, m, 1):
                        for i in range(0, n, 1):
                            if notes[i][j] == b'*':
                                plus_j[j] = '+'
        else:
            min_not_mark_elem = 10000
            for j in range(0, m, 1):
                for i in range(0, n, 1):
                    if plus_i[i] != b'+' and plus_j[j] != b'+':
                        if c_0[i][j] < min_not_mark_elem:
                            min_not_mark_elem = c_0[i][j]
            if min_not_mark_elem == 10000:
                list_i = []
                list_j = []
                for i in range(0, n, 1):
                    for j in range(0, m, 1):
                        if notes[i][j] == b'*':
                            list_i.append(i)
                            list_j.append(j)
                return list_i, list_j
            else:
                for j in range(0, m, 1):
                    if plus_j[j] == b'+':
                        for i in range(0, n, 1):
                            c_0[i][j] += min_not_mark_elem
                for i in range(0, n, 1):
                    if plus_i[i] != b'+':
                        for j in range(0, m, 1):
                            c_0[i][j] -= min_not_mark_elem


if __name__ == "__main__":
    table = np.array([[12, 2, 4, 2, 1, 0],
                      [5, 9, 6, 6, 3, 7],
                      [7, 2, 2, 3, 4, 5],
                      [2, 8, 8, 9, 0, 2],
                      [0, 4, 4, 8, 6, 4],
                      [4, 3, 1, 5, 2, 3]])
    print("Производительность:\n", table)
    list_i, list_j = hungarian_method(table)
    print("Максимальная производительность обеспечивается, если\n")
    C_max = 0
    for k in range(0, len(list_i), 1):
        print("Работник", list_i[k]+1, "выполняет задачу", list_j[k]+1)
        C_max += table[list_i[k]][list_j[k]]
    print("\nМаксимальная производительность =", C_max)
