"""

\d любая цифра [0-9]
\D любая НЕ цифра
\w любой алфавитный символ [A-Z a-z]
\W любой НЕ алфавитный символ НЕ [A-Z a-z]
\s пробел
\S НЕ пробел
\. = .

[0-9][0-9][0-9] = [0-9]{3} = \d{3}

[A-Z][a-z]+

[a-z]+ = сколько угодно маленьких алфавитных символов

"""

# import sys
import re

fin = open('task1_input.txt')
fou = open('task1_output.txt', mode='w')
ls = (fin.read())
print(ls)

# findtext = r"\b[A-Z][a-z]{2,9}\b"
findtext = r"(?:(?<=^)|(?<=\s))([A-Z][a-z]{2,9})(?:(?=\s)|(?=\,)|(?=\:)|(?=\;)|(?=\.)|(?=$))"
res = re.findall(findtext, ls, re.MULTILINE)
# res = re.findall(findtext, ls)
print(res)
print(len(res))

resstr = 'Слова: '
for s in res:
    resstr = resstr + s + ', '
fou.write(str(resstr[:-2] + '.'))







