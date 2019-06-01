import json
import csv


def dicttocsv(dct, ls):
    for d in dct:
        ls.append([d, dct[d]])
        if str(type(dct[d])) == "<class 'dict'>":
            dicttocsv(dct[d], ls)
    pass


def task7_2(jsf, csvf):
    with open(jsf, 'r') as jsf:
        d1 = json.load(jsf)
        jsf.close()
    ls = []
    with open(csvf, 'w') as csvf:
        wrr = csv.writer(csvf)
        dicttocsv(d1, ls)
        for l in ls:
            wrr.writerow(l)
        csvf.close()
    pass


task7_2('test.json', 'test.csv')




