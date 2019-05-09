st = 'JanFebMarAprMayJunJulAugSepOctNovDec'
num = int(input("Введите номер месяца: "))

if num > 12 or num < 1:
    raise ValueError('Номер месяца должен быть от 1 до 12')


def task_12(s, n):
    n1 = (int(n) - 1) * 3
    n2 = n1 + 3
    return s[n1:n2]


print(task_12(st, num))
