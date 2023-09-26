cache = {1: 1, 2: 1}


def fib(n):
    res = (lambda x: cache[x] if x in cache else cache.setdefault(x, fib(x - 1) + fib(x - 2)))(n)
    return res


print(fib(1))
print(fib(2))
print(fib(5))
