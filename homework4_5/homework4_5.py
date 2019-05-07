from decimal import Decimal
from collections import defaultdict, namedtuple

lst = [
    ('Вася', 'Иванов', (10, 8, 6)),
    ('Иван', 'петров', (10, 10, 9, 9)),
    ('владимир', 'иванов', (4, 5, 6))
]

std = namedtuple('Student', ['name', 'surname', 'average_mark'])

result = defaultdict(list)
dd = defaultdict()
for n, s, m, in lst:
    result[(n[0]+s[0]).upper()] += [std(n, s, Decimal(sum(m)/len(m)))]
print(result)

