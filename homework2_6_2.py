str="abztaba"

def task_6(s):
    print(s)

    l = len(s)//2

    result = True
    for i in range(l):

        print(s[i], s[~i])

        if s[i] != s[~i]:
            result = False
            break
    return result

print(task_6(str))
