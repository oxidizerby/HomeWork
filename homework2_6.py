str="abataca"

def task_6(s):
    print(s)

    l = len(s)

    result = True
    for i in range(l//2):
        l-=1
        print(s[i], s[l])

        if s[i] != s[l]:
            result = False
            break
    return result

print(task_6(str))
