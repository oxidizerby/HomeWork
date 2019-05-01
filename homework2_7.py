#str="Дядя Семён ехал "
str="Дядя Семён ехал из города домой. С ним была собака Жучка."

def task_7(s):
    print(s)
    l = len(s)
    while l > 40:
        l = s.rfind(" ")
        s = s[:l]
        print(s, l)
    return s

print(task_7(str))
