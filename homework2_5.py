str = "Шла Саша по шоссе и сосала сушку"

def task_5(str):
    i1=str.find("а")
    i2=str.rfind("а")
    
    str1 = str[:i1+1]
    str2 = str[i1+1:i2]
    str3 = str[i2:]
    
    str2 = str2.replace("а","А")
    str = str1 + str2 + str3
    return str

#print("Результат: ","\""+task_3(str)+"\"")
print(f"Результат: \"{task_5(str)}\"")
