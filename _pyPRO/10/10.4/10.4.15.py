from random import randint as rnd

class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n
        self.arr = [rnd(self.left, self.right) for _ in range(self.n)]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.arr:
            raise StopIteration
        else:
            return self.arr.pop()




iterator = RandomNumbers(1, 1, 3)

print(next(iterator))
print(next(iterator))
print(next(iterator))


iterator = RandomNumbers(1, 10, 2)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))

iterator = RandomNumbers(-1000, -900, 1)

print(next(iterator) in range(-1000, -899))

try:
    next(iterator)
except StopIteration:
    print('Error')