from itertools import dropwhile, compress


def first_true(iterable, predicate=None):
    res = list(filter(predicate, iterable))
    if res:
        return res[0]
    else:
        return None


numbers = [1, 1, 1, 1, 2, 4, 5, 6]

print(first_true(numbers, lambda num: num % 2 == 0))

numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])

print(first_true(numbers, lambda num: num > 10))

numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)

print(first_true(numbers, None))