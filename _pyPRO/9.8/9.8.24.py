import functools


def ignore_exception(*args_deco):
    def ignore_exception_deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
                return res
            except Exception as ex:
                if type(ex) in args_deco:
                    print(f'Исключение {type(ex).__name__} обработано')
                else:
                    raise ex
        return wrapper
    return ignore_exception_deco


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x


f(0)

min = ignore_exception(ZeroDivisionError)(min)

try:
    print(min(1, '2', 3, [4, 5]))
except Exception as e:
    print(type(e))