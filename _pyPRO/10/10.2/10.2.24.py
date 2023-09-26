def get_min_max(iterable):
    a = None
    b = None
    for it in iterable:
        if a is None:
            a = it
        if b is None:
            b = it
        if a > it:
            a = it
        if b < it:
            b = it
    if a is not None:
        return a, b
    else:
        return None


iterable = iter(range(10))

print(get_min_max(iterable))

iterable = [6, 4, 2, 33, 19, 1]

print(get_min_max(iterable))

iterable = iter([])

print(get_min_max(iterable))