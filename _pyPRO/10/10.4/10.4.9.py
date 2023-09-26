class Square:
    def __init__(self, n: int):
        self.n = n
        self.k = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n and self.n > 0:
            self.n -= 1
            self.k += 1
            return self.k**2
        else:
            raise StopIteration


squares = Square(2)

print(next(squares))
print(next(squares))

squares = Square(10)

print(list(squares))


squares = Square(1)

print(list(squares))