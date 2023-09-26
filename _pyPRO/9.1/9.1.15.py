def zip_longest(*args, fill=None):
    if not any(map(lambda x: len(x), args)):
        return []
    to_fill = len(max(*args, key=len))
    lists = []
    for arg in args:
        if len(arg) < to_fill:
            arg.extend([fill]*(to_fill - len(arg)))
            lists.append(arg)
        else:
            lists.append(arg)
    return list(zip(*lists))


print(zip_longest([1, 2, 3, 4, 5], ['a', 'b', 'c'], fill='_'))

data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))

data = [[1, 2, 3, 4, 5], ['one', 'two', 'three', 'four', 'five'], ['I', 'II', 'III', 'IV', 'V']]
print(zip_longest(*data))

data = [[]]
print(zip_longest(*data, fill='not known'))
