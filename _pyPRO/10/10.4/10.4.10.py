class Fibonacci:
    def __init__(self):
        self.fib = [0, 1]
        self.next = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.fib.append(self.fib[-1] + self.fib[-2])
        self.next += 1
        return self.fib[self.next]


fibonacci = Fibonacci()

print(next(fibonacci))

fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

fibonacci = Fibonacci()

print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))