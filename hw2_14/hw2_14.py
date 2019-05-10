st = '  Василий Пупкин '


def task_14(s):

    # Обрезаем лишние пробелы по краям
    while s[0] == ' ' or s[-1] == ' ':
        if s[0] == ' ':
            s = s[1:]
        if s[-1] == ' ':
            s = s[:-1]

    # Проверяем количество слов
    if s.find(' ') != s.rfind(' ') or s.find(' ') == -1:
        raise ValueError("Не два слова!")

    res = ''
    i = len(s) - 1
    while s[i] != ' ':
        res += s[i]
        i = i - 1

    return s[0] + '. ' + res[::-1]


print(task_14(st))
