str = "Шла Саша по шоссе и сосала сушку"

def task_4(str):
    i1=str.find("а")
    i2=str.rfind("а")
    str = str[:i1] + str[i2+1:]
    return str

#print("Результат: ","\""+task_3(str)+"\"")
print(f"Результат: \"{task_4(str)}\"")
