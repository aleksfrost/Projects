import functools


def strip_range(start, end, char='.'):
    def strip_range_deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if start > len(res):
                return res
            elif end > len(res):
                return res[:start] + char*(len(res) - start)
            else:
                return res[:start] + char*(end - start) + res[end:]
        return wrapper
    return strip_range_deco


@strip_range(3, 5)
def beegeek():
    return 'beegeek'


print(beegeek())


@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'


print(beegeek())


@strip_range(20, 30)
def beegeek():
    return 'beegeek'


print(beegeek())


