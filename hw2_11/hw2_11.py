lst = [2, 3, 4, 5, 3, 4, 5, 7, 8, 6, 4, 3, 4, 7, 8, 1]
num = 3


def task_11(lst, num):
    n = 0
    for i in lst:
        if i == num:
            n += 1
    return n


print(task_11(lst, num))
