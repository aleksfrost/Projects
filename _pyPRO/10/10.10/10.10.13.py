from itertools import chain


def sum_of_digits(iterable):
    res = sum((int(num) for num in chain.from_iterable(str(num) for num in iterable)))
    return res




print(sum_of_digits([13, 20, 41, 2, 2, 5]))

print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))


print(sum_of_digits([123456789]))