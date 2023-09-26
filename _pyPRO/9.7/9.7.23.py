def exception_decorator(func):
    def decor(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
            return (res, 'Функция выполнилась без ошибок')
        except Exception:
            return (None, 'При вызове функции произошла ошибка')
    return decor


@exception_decorator
def f(x):
    return x ** 2 + 2 * x + 1


print(f(7))


sum = exception_decorator(sum)

print(sum(['199', '1', 187]))