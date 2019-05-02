import random

n = 0
for i in range(100):
    l = [random.choice([1, 2, 3, 4, 5, 7]) for i in range(2)]
    if l[0] == l[1]:
        print(l, "____________________________!!!")
        n+=1
    else: print(l)

    l = [1, 2, 3, 4, 5, 7]
    random.shuffle(l)
    print(l[0], l[1], "\n", )

print("Итого", n, "раз из 100")
