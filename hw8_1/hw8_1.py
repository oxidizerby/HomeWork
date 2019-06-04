class Task1D(object):
    x = 3


class Task1C(Task1D):
    x = 1
    pass


class Task1B(Task1C):
    pass


class Task1A(Task1B):  # +
    x = 2


class Task1E(Task1D):  # +
    pass


obj = Task1A()

print(obj.x)











