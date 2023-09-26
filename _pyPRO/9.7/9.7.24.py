def takes_positive(func):
    def decor(*args, **kwargs):
        if any(isinstance(x, float) for x in args) or any(isinstance(x[1], float) for x in kwargs.items()):
            raise TypeError
        elif any(x < 1 for x in args) or any(x[1] < 1 for x in kwargs.items()):
            raise ValueError
        else:
            res = func(*args, **kwargs)
        return res
    return decor


@takes_positive
def positive_sum(*args):
    return sum(args)


print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(*range(100, -1, -1)))
except Exception as err:
    print(type(err))