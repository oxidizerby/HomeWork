d = {'aaa': [1, 2, 7, 9, 10], 'bbb': [1, 2, 3, 4], 'ccc': [8, 9, 10], 'ddd': [7, 7, 7], 'eee': [1, 2, 7, 9, 10], 'fff': [8, 9, 10], 'ggg': [10], 'hhh': [5], 'iii': [6], 'iii': [8]}
print(d)

def task_18(d):
    l = []
    for i in d:
        n = 0
        sr = 0
        for j in d[i]:
            #print(j)
            if type(j) != type(1):
                raise TypeError ("Не верный тип оценки. Должен быть int", j)
            if (10<j or j<0):
                raise ValueError ("оценка не может быть < 0 и/или > 10", j)
            n += 1
            #try:
            sr += j
            #except TypeError:
            #    print(f"Не верный формат оценки \"{j}\" в {i} {d[i]}. Оценка не будет учтена.")
        sr = sr / n
        #print(sr)
        if sr >= 4: 
            t = (i, sr)
            #print(t)

            # Сортировка
            ii=0
            for m in l:
                if sr < m[1]:
                    ii+=1
            l.insert(ii, t)

    return l

print("Результат: ", task_18(d))

'''
564889
5
65
654
8654
88654
988654
'''
