
st = 'abcdefghijklmnopqrstuvwxyz'


def task_8(s):
    res1 = s[2]
    res2 = s[-2]
    res3 = s[:5]
    res4 = s[:-2]
#    res5 = str([i for i in s[::2] if i != ' '])
    res5 = ''
    for i in s[::2]:
        if i != ' ':
            res5 += i

    res6 = str([i for i in s[1::2] if i != ' '])
    res7 = st[::-1]
    res8 = st[::-2]
    res9 = len(st)
    return res1, res2, res3, res4, res5, res6, res7, res8, res9


print(task_8(st))