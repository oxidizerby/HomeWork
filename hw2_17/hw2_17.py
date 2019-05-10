mas = [1, 5, 4, 7, 4, 2, 3, 4, 7, 9, 8, 7, 10, 2, 3, 1, 2, -10, 0]


def task_17(m):
    dt = {'Errors': 0}
    st = set(m)
    print(st)
    for k in st:
        if k < 1 or k > 10:
            dt['Errors'] = dt['Errors'] + 1
        else:
            dt[k] = 0
    for i in m:
        if 11 > i > 0:
            dt[i] = dt[i] + 1

    return dt


print(task_17(mas))
