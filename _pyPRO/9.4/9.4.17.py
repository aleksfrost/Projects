def polynom(x):
    res = x**2 + 1
    polynom.__dict__.setdefault('values', set()).add(res)
    return res


print(polynom(5))
print(polynom.values)

polynom.values = set()

polynom(1)
polynom(2)
polynom(3)

print(*sorted(polynom.values))
polynom.values = set()
for _ in range(10):
    polynom(10)

print(polynom.values)