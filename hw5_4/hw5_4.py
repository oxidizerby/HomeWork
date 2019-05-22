from decimal import Decimal
import collections


def decor(f):
    def wrapper(*args, **kwargs):
        newargs = []
        for a in args[:5]:
            ta = str(type(a))
            if ta == "<class 'bool'>":
                newargs.append(not a)
            elif isinstance(a, str) or isinstance(a, list):
                newargs.append(a[::-1])
            elif ta == "<class 'decimal.Decimal'>" or ta == "<class 'int'>" or ta == "<class 'float'>":
                newargs.append(-a)
            elif ta == "<class 'dict'>":
                # print(a)
                newargs.append({k[::-1]: a[k] for k in a})
            else:
                newargs.append(a)

        newkwargs = {}
        for a in kwargs:
            b = kwargs[a]
            ta = str(type(b))
            if ta == "<class 'bool'>":
                newkwargs[a] = not b
            elif isinstance(b, str) or isinstance(b, list):
                newkwargs[a] = b[::-1]
            elif ta == "<class 'decimal.Decimal'>" or ta == "<class 'int'>" or ta == "<class 'float'>":
                newkwargs[a] = -b
            elif ta == "<class 'dict'>":
                newkwargs[a] = ({k[::-1]: b[k] for k in b})
            else:
                newkwargs[a] = b
        newkwargs = collections.OrderedDict(sorted(newkwargs.items(), key=lambda k: k[0])[:5])
        f(*newargs, **newkwargs)
    return wrapper


@decor
def funk(*arg, **narg):
    print('---------------')
    print(arg)
    print(narg)


dc = Decimal('55')
di = {'key1': 'znach1', 'key2': 'znach2'}
dct = {'m': 5, 'n': 3, 'o': 'asd', 'p': 0, 'l': di, 'q': 0, 'r': 0, 'k': 0}
funk('sd', [1, 2, 3], True, dc, di, 58.76, 59, **dct)




