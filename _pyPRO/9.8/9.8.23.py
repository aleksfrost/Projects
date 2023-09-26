import functools


def add_attrs(**kwargs_new):
    def add_attrs_deco(func):
        for key in kwargs_new:
            func.__dict__[key] = kwargs_new[key]
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res
        return wrapper
    return add_attrs_deco


@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)


@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)


