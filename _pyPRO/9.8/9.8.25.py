import functools


class MaxRetriesException(Exception):
    pass


def retry(times):
    def retry_deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal times
            while times:
                try:
                    res = func(*args, **kwargs)
                    return res
                except Exception:
                    times -= 1
            raise MaxRetriesException
        return wrapper
    return retry_deco


@retry(3)
def no_way():
    raise ValueError


try:
    no_way()
except Exception as e:
    print(type(e))


@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')


beegeek()
