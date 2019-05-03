from datetime import *

def task_4(d1, d2):

    assert isinstance(d1, datetime)
    assert isinstance(d2, datetime)

    print(d1)
    print(d2)

    d = d2 - d1

    dme = d2.month - d1.month
    dl = d2.year - d1.year
    dch = d.days * 24 + d2.hour - d1.hour
    dmi = dch * 60 + d2.minute - d1.minute

    ned = d.days // 7
    vek = dl // 100
    mes = (dl * 12) + dme
    sec = dmi * 60 + d2.second - d1.second

#    print("Веков", vek)
#    print("Лет:", dl)
#    print("Месяцев:", mes)
#    print("Недель:", ned)
#    print("Дней:", d.days)
#    print("Часов:", dch)
#    print("Минут:", dmi)
#    print("Секунд:", sec)

    return vek, dl, mes, ned, d.days, dch, dmi, sec

date1 = datetime(1590, 4, 27, 19, 24, 20, 430155)
date2 = datetime(2019, 5, 29, 20, 30, 21, 430160)

print(task_4(date1, date2))
