def unique(iterable):
    mem = []
    [mem.append(i) for i in iterable if i not in mem]
    yield from mem


numbers = [1, 2, 2, 3, 4, 5, 5, 5]

print(*unique(numbers))


iterator = iter('111222333')
uniques = unique(iterator)

print(next(uniques))
print(next(uniques))
print(next(uniques))

data = map(abs, range(-100, 100))

print(*unique(data))