
def task_1(a, *args, **nargs):
    mres1 = []
    mres2 = {}
    for i in args:
        mres1.append((a == i, type(a) == type(i)))
    for n in nargs:
        mres2[n] = (nargs[n] == a, type(nargs[n]) == type(a))

    return mres1, mres2


print(task_1(5, 1, 2, 3, 4, x=1, y=2, z=5, w='asd'))
# print(task_1(5))
