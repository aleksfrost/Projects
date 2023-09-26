from itertools import cycle


def alnum_sequence():
    return cycle(a for all in zip([i for i in range(1, 27)], [chr(i) for i in range(ord("A"), ord("Z")+1)]) for a in all)


alnum = alnum_sequence()

print(*(next(alnum) for _ in range(55)))


alnum = alnum_sequence()

print(*(next(alnum) for _ in range(100)))