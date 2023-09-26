class Repeater:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        if self.obj is not None:
            return self.obj



bee = Repeater('bee')

print(next(bee))


geek = Repeater('geek')

print(next(geek))
print(next(geek))
print(next(geek))


