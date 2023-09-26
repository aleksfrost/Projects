from itertools import pairwise


def max_pair(iterable):
    a = map(lambda x: x[1] + x[0], pairwise(iterable))
    res = next(a)
    for n in a:
        if n > res:
            res = n
    return res


print(max_pair([1, 8, 2, 4, 3]))

iterator = iter([1, 2, 3, 4, 5])

print(max_pair(iterator))


iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])

print(max_pair(iterator))