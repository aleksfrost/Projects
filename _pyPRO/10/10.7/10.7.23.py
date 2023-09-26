def around(iterable):
    if iterable:
        prev = None
        it = iter(iterable)
        start = next(it)
        for nekst in it:
            res = (prev, start, nekst)
            prev, start = start, nekst
            yield res
        yield prev, start, None
    else:
        return


numbers = [1, 2, 3, 4, 5]

print(*around(numbers))

iterator = iter('hey')

print(*around(iterator))

