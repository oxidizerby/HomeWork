import requests
from datetime import datetime, timedelta
import locale
import re


def deltag(deltags, text):
    for tag in deltags:
        regextag = fr"<{tag}.*?>"
        lst = re.findall(regextag, text)
        lst.append(f"</{tag}>")
        lst = list(set(lst))
        for find in lst:
            text = text.replace(find, '')
    return text


req = requests.get('http://meteoinfo.by/5/')
st = req.text

f1 = '>Время в Минске '
st = st[st.find(f1) + len(f1):]
dtweb = st[:st.find('<br>')]
locale.setlocale(locale.LC_TIME, ('ru_RU', 'UTF-8'))
today = datetime.strptime(dtweb, '%H:%M; %d %B %Y')
tomorrow = today + timedelta(days=1)

today_str = today.strftime('%A, %d %B')
tomorrow_str = tomorrow.strftime('%A, %d %B')
print(today_str)

# f1 = today_str
f1 = "id='26850'>"
st = st[st.find(f1):]

st = deltag(('font',), st)
f1 = tomorrow_str
st = st[:st.find(f1) + len(f1)]

st = st.replace('<br>', ' ')
st = st.replace('<BR>', ' ')

tags = ('nobr', 'b', 'span', 'img', 'strong', 'sup', 'a', 'u')
st = deltag(tags, st)
st = st.replace('&#176;', 'градусов ')

regex = r"<tr([\s\S]*?)<\/tr>"
lt = re.findall(regex, st)

regex = r"<td.*?>([\s\S]*?)<\/td>"
tofile = []
for l in lt:
    result = []
    res = re.findall(regex, l)
    for rr in res:
        if rr == 'Дата и время суток':
            result.append('Время суток')
        elif rr != '':
            result.append(rr)
    tofile.append(result)

col = len(tofile[0])
row = len(tofile)

writelst = []
for c in range(6):
    for r in range(1, row):
        print(tofile[0][c], ' --- ', tofile[r][c])
        writelst.append(tofile[0][c] + ' --- ' + tofile[r][c] + '\n')

with open('file.txt', 'w') as file:
    file.write(today_str + '\n'*2)
    file.writelines(writelst)

