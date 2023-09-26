from itertools import islice


def take_nth(iterable, n):
    k = None
    if n == 1:
        return next(iterable)
    elif n < 0:
        return None
    res = list(islice(iterable, 0, n+1, n-1))
    try:
        return res[1]
    except IndexError:
        return None


numbers = [11, 22, 33, 44, 55]

print(take_nth(numbers, 3))


iterator = iter('beegeek')

print(take_nth(iterator, 4))

iterator = iter('beegeek')

print(take_nth(iterator, 10))

iterator = iter('beegeek')

print(take_nth(iterator, 1))