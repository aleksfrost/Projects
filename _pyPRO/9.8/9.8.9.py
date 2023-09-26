import functools


def square(func):
    @functools.wraps(func)
    def decor(*args, **kwargs):
        return func(*args, **kwargs)**2
    return decor

@square
def add(a, b):
    return a + b

print(add(3, 7))

@square
def add(a, b):
    '''прекрасная функция'''
    return a + b

print(add(1, 1))
print(add.__name__)
print(add.__doc__)