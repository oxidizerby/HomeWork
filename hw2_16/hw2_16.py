mas = [1, 10, 20, 75, 30, 23, 50, 11, 45, 54]


def task_16(m):
    for t in mas:
        if not isinstance(t, int):
            raise TypeError('В массиве есть значение не формата int')
    s = 0
    i = 0
    while s <= 100 and i < len(m):
        if m[i] % 10 != 0:
            s += m[i]
        print(i, m[i], s)
        i += 1
    if s < 100:
        raise ValueError('Мало чисел в массиве, сумма не достигла 100!')
    return s


print(task_16(mas))