# lst = [[[1, 2, 3], [4, 1], [2, 5]], [[1, 6], [2, 7]], [[1, 8]]]
# print(lst)

# for i in lst:
#     for n in i:
#         for m in n:
#             lst1.append(m)

print(sorted(list(set([m for i in [[[1, 2, 3], [4, 1], [2, 5]], [[1, 6], [2, 7]], [[1, 8]]] for n in i for m in n])), reverse=True))
