def with_previous(iterable):
    j = None
    for i in iterable:
        res = (i, j)
        j = i
        yield res

numbers = [1, 2, 3, 4, 5]

print(*with_previous(numbers))

iterator = iter('stepik')

print(*with_previous(iterator))