import random


def random_numbers(left, right):
    infinite_rand = iter(lambda: random.randint(left, right), 1.5)
    return infinite_rand


iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))


iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))


