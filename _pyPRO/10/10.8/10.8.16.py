import operator
from itertools import accumulate


def factorials(n):
    yield from list(accumulate(range(1, n+1), operator.mul))



numbers = factorials(6)

print(*numbers)

numbers = factorials(2)

print(next(numbers))
print(next(numbers))