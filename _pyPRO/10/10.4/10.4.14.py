class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.it_len = len(iterable)
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        res = self.iterable[self.start]
        self.start += 1
        if self.start == self.it_len:
            self.start = 0
        return res



cycle = Cycle('be')

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))


cycle = Cycle([1])

print(next(cycle) + next(cycle) + next(cycle))


cycle = Cycle(range(100_000_000))

print(next(cycle))
print(next(cycle))
