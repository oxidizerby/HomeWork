x = 712345

def task_10(x):
    d = len(str(x)) #Длина числа

    i1 = x//(10**(d-1)) #Первое число
    b1 = 3<=i1<=8

    #Второй способ
    s = str(x)
    y = int(s[0])
    b2 = 3<=y<=8
    
    return d, b1, b2

print(f"Результат: {task_10(x)}")
