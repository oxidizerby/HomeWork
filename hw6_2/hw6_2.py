import os


def finf(p, n=-1):
    n += 1
    ls = os.listdir(p)
    dd = {'FOLDERS': {}, 'FILES': {}}
    d = {}
    for name in ls:
        fname = os.path.join(p, name)
        if os.path.isdir(fname):
            print('\t'*n + 'FOLDER: ' + name)
            d[name] = finf(fname, n)
            dd['FOLDERS'] = d
        if os.path.isfile(fname):
            ff = os.path.splitext(name)[1][1:]
            d[name] = {'Format': ff, 'Size': str(os.stat(fname).st_size)}
            print('\t'*n + 'file: ' + name)
            print('\t' * (n+1) + 'Format: ' + ff)
            print('\t' * (n+1) + 'Size: ' + str(os.stat(fname).st_size))
            if ff.lower() == 'txt':
                fsb = open(fname)
                fsb.seek(0, 2)
                print('\t' * (n + 1) + 'Length: ' + str(fsb.tell()))
                d[name]['Length'] = str(fsb.tell())
                fsb.close()
            dd['FILES'] = d
    return dd


print(finf('./venv'))


