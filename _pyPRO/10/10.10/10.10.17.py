def grouper(iterable, n):




numbers = [1, 2, 3, 4, 5, 6]

print(*grouper(numbers, 2))

iterator = iter([1, 2, 3, 4, 5, 6, 7])

print(*grouper(iterator, 3))

iterator = iter([1, 2, 3])

print(*grouper(iterator, 5))