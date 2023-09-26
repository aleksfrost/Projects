def do_twice(func):
    def decor(*args, **kwargs):
        res = func(*args, **kwargs)
        func(*args, **kwargs)
        return res
    return decor


@do_twice
def beegeek():
    print('beegeek')


beegeek()


@do_twice
def beegeek():
    print('beegeek')


print(beegeek())