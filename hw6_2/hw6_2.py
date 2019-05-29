import os


def finf(p):
    ls = os.listdir(p)
    dd = {'FOLDERS': {}, 'FILES': {}}
    dfolder = {}
    dfile = {}
    for name in ls:
        fname = os.path.join(p, name)
        if os.path.isdir(fname):
            dfolder[name] = finf(fname)
            dd['FOLDERS'] = dfolder
        if os.path.isfile(fname):
            ff = os.path.splitext(name)[1][1:]
            dfile[name] = {'Format': ff, 'Size': str(os.stat(fname).st_size)}
            if ff.lower() == 'txt':
                fsb = open(fname)
                fsb.seek(0, 2)
                dfile[name]['Length'] = str(fsb.tell())
                fsb.close()
            dd['FILES'] = dfile
    return dd


def printdict(prndtc, tabs):
    tabs += 1
    for prn in prndtc:
        if str(type(prndtc[prn])) == "<class 'dict'>":
            print('\t' * tabs, prn)
            printdict(prndtc[prn], tabs)
        else:
            print('\t' * tabs, prn, prndtc[prn])
    pass


pch = finf('./venv/lib/python3.7/site-packages/pip-19.0.3-py3.7.egg/pip/_internal')
print(pch)
printdict(pch, -1)

