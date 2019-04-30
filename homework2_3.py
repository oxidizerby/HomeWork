str = "Привет, мир!"

def task_3(str):
    i=str.find(" ")
    str = str[i+1:] + str[i] + str[:i]
    return str

#print("Результат: ","\""+task_3(str)+"\"")
print(f"Результат: \"{task_3(str)}\"")
