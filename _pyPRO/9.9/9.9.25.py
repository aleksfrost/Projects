# How many ways to step "n" by 1, 3 or 4 steps

from functools import lru_cache


@lru_cache
def ways(n: int):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 1
    if n == 4:
        return 2
    if n < 0:
        return 0
    if n - 4 > 0:
        return ways(n-1) + ways(n-3) + ways(n-4)


print(ways(1))
print(ways(2))
print(ways(5))
print(ways(50))
print(ways(100))



