class DictItemsIterator:
    def __init__(self, data: dict):
        self.data = data
        self.half = list(data)
        self.half_res = iter(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        half_res = next(self.half_res)
        if half_res:
            return half_res, self.data[half_res]
        else:
            raise StopIteration


pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})

print(*pairs)


data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}

pairs = DictItemsIterator(data)

print(*pairs)


data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

pairs = DictItemsIterator(data)

print(tuple(pairs))

try:
    print(next(pairs))
except StopIteration:
    print('Error')

