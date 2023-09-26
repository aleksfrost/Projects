class PowerOf:
    def __init__(self, number: float):
        self.number = number
        self.k = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number != 0:
            res = self.number ** self.k
            self.k += 1
            return res
        else:
            raise StopIteration


power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))