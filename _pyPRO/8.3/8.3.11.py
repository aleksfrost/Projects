def get_fast_pow(a: int, n: int) -> int:
    if n == 0:
        return 1
    else:
        if n % 2 == 0:
            return get_fast_pow((a * a), n//2)
        elif n % 2 == 1:
            return a * get_fast_pow(a, n-1)


print(get_fast_pow(2, 10))
print(get_fast_pow(5, 2))
print(get_fast_pow(2, 100))
