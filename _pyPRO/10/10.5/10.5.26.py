def palindromes(i=None, res=None):
    if i is None:
        i = 1
    while True:
        a = [k for k in str(i)]
        b = a[::-1]
        if a == b:
            yield i
        i += 1




generator = palindromes()

print(next(generator))
print(next(generator))
print(next(generator))


generator = palindromes()
numbers = [next(generator) for _ in range(30)]

print(*numbers)