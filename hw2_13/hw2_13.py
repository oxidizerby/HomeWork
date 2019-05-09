tp = (28, 12, 2019)


def task_13(t):
    st = ''
    for i in range(len(t)):
        st += str(t[i])
        if i < len(t)-1:
            st += '-'
    return st


print(task_13(tp))
