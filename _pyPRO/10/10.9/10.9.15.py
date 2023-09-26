from itertools import compress


def take(iterable, n):
    res = list(compress(iterable, [True]*n))
    yield from res


print(*take(range(10), 5))

iterator = iter('beegeek')

print(*take(iterator, 22))

iterator = iter('beegeek')

print(*take(iterator, 1))