def all_together(*args):
#    for arg in args:
#        yield from arg
    return (ark for arg in args for ark in arg)




objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]

print(*all_together(*objects))


objects = [[1, 2, 3], [(0, 0), (1, 1)], {'geek': 1}]

print(*all_together(*objects))


print(list(all_together()))