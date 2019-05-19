from decimal import Decimal
from functools import reduce

intmas = list(range(-3, 103))
print(intmas)

task_2_a = lambda x: x % 10 > 0 == x % 2 == 0 < x < 100
mass = list(filter(task_2_a, intmas))
print(mass)


task_2_b = lambda y: int(y / 2) if y % 2 == 0 else int(y * 2)
mass = list(map(task_2_b, intmas))
print(mass)


#task_2_c =


# decmas = [-5.23, 12.3223, 34.23432]
decmas = [-3, -2, -1, 0, 1.02, 2.23, 3, 4, 5]
print(decmas)

# task_2_d = lambda z: Decimal(reduce(lambda a, b: a + b, list(filter(lambda z1: z1 > 0, z))) / len(list(filter(lambda z1: z1 > 0, z))))
# task_2_d = lambda z: Decimal(sum(list(filter(lambda z1: z1 > 0, z))) / len(list(filter(lambda z1: z1 > 0, z))))
task_2_d = lambda z: Decimal(sum([z1 for z1 in z if z1 > 0]) / len([z1 for z1 in z if z1 > 0]))

d = task_2_d(decmas)
print(type(d))
print(d)



