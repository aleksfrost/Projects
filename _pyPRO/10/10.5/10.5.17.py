def primes(left, right):
    if left == 1:
        left = 2
    for k in range(left, right+1):
        if all(map(lambda x: k % x, range(2, k//2+1))):
            yield k



generator = primes(1, 15)

print(*generator)


generator = primes(6, 36)

print(next(generator))
print(next(generator))