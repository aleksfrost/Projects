from itertools import dropwhile


def drop_this(iterable, obj):
    new_numbers = list(dropwhile(lambda elem: elem == obj, iterable))
    yield from new_numbers


numbers = [0, 0, 0, 1, 2, 3]

print(*drop_this(numbers, 0))


iterator = iter('bbbbeebee')

print(*drop_this(iterator, 'b'))


iterator = iter('ssssssssssssssssssssssss')

print(list(drop_this(iterator, 's')))