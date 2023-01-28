import math


def zeros(n):
    if n == 0 or n == 1:
        return 0
    else:
        k_max = int(round(math.log(n, 5), 0))
        z = sum([int(round(n / 5**i, 0)) for i in range(1, k_max+1)])
        return z


assert zeros(0) == 0
assert zeros(6) == 1
assert zeros(30) == 7
