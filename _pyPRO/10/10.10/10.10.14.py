from itertools import pairwise


def is_rising(iterable):
    a = map(lambda x: x[1] > x[0], (pair for pair in pairwise(iterable)))
    if a:
        return all(a)
    else:
        return False


print(is_rising([1, 2, 3, 4, 5]))

iterator = iter([1, 1, 1, 2, 3, 4])

print(is_rising(iterator))

iterator = iter(list(range(100, 200)))

print(is_rising(iterator))