def get_pow(a: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        n -= 1
        return a * get_pow(a, n)


print(get_pow(2, 10))
print(get_pow(5, 2))
print(get_pow(2, 100))

