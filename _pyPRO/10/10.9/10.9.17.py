from itertools import takewhile

"""
def first_largest(iterable, number):
    real = list(iterable)
    res = list(takewhile(lambda x: x <= number, real))
    if len(real) == len(res):
        return -1
    else:
        return len(res)
"""

def first_largest(iterable, number):
    for i, value in enumerate(iterable):
        if value > number:
            return i
    return -1

numbers = [10, 2, 14, 7, 7, 18, 20]

print(first_largest(numbers, 11))

iterator = iter([-1, -2, -3, -4, -5])

print(first_largest(iterator, 10))

iterator = iter([18, 21, 14, 72, 73, 18, 20])

print(first_largest(iterator, 10))

iterator = iter([18, 21, 14, 72, 73, 18, 20, 101, 102, 110])

print(first_largest(iterator, 105))