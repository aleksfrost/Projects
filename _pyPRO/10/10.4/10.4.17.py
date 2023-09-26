class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0:
            if self.start >= self.end:
                raise StopIteration
            else:
                res = self.start
                self.start = self.start + self.step
                return res
        if self.step < 0:
            if self.start <= self.end:
                raise StopIteration
            else:
                res = self.start
                self.start = self.start + self.step
                return res






evens = Xrange(0, 10, 2)

print(*evens)


xrange = Xrange(0, 3, 0.5)

print(*xrange, sep='; ')

xrange = Xrange(10, 1, -1)

print(*xrange)

xrange = Xrange(5, 10)

print(*xrange)