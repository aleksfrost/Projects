import functools


def prefix(string, to_the_end=False):
    def prefix_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if to_the_end:
                return func(*args, **kwargs) + string
            else:
                return string + func(*args, **kwargs)
        return wrapper
    return prefix_decorator


@prefix('€')
def get_bonus():
    return '2000'


print(get_bonus())


@prefix('$$$', to_the_end=True)
def get_bonus():
    return '2000'


print(get_bonus())


@prefix('online-school ')
def make_lower(string, lower=True):
    '''makes string upper or lower'''
    if lower:
        return string.lower()
    return string.upper()


print(make_lower.__name__)
print(make_lower.__doc__)
print(make_lower('beegeek', False))


