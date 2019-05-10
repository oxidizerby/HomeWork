x = 5


def task_15(f):
    if not isinstance(f, int):
        raise TypeError('Не верный тип входных данных')
    if f < 0:
        raise ValueError("Введено отрицательное число!")

    res = 1
    for i in range(1, f + 1):
        res = res * i
    return res


print(task_15(x))
