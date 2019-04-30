def task_2(str):
    #str = input("Введите строку: ")
    #print("Вы ввели: ", str)

    i = len(str)
    print("Длина строки: ", i)

    i1 = i//2
    print("Длина первой части строки: ", i1)

    str1 = str[0:i1]
    print("Первая часть строки: ", str1)

    str2 = str[i1:i]
    print("Вторая часть строки: ", str2)

    str3 = str2 + str1
    #print("Меняем строки местами: ", str3)

    return str, str3

#task_2(input("Введите строку: "))
print("Результат: ", task_2(input("Введите строку: ")))
