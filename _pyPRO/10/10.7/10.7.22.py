def pairwise(iterable):
    if iterable:
        it = iter(iterable)
        start = next(it)
        for i in it:
            res = (start, i)
            start = i
            yield res
        yield start, None
    else:
        return []


numbers = [1, 2, 3, 4, 5]

print(*pairwise(numbers))

iterator = iter('stepik')

print(*pairwise(iterator))

print(list(pairwise([])))