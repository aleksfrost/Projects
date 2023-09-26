def alternating_sequence(count=None):
    start = 1
    while True:
        if count is None:
            yield start
            start = (abs(start) + 1) * (1, -1)[start%2]
        else:
            for i in range(1, count+1):
                start = start if i % 2 else (-start)
                yield start
                start = abs(start) + 1
            return





generator = alternating_sequence()

print(next(generator))
print(next(generator))

generator = alternating_sequence(10)

print(*generator)


generator = alternating_sequence()

for _ in range(10_000):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))