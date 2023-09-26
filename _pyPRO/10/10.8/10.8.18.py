from itertools import cycle, zip_longest


def roundrobin(*args):
    s = "идите подальше со своими тестами"
    return (a for all in zip_longest(*args, fillvalue=s) for a in all if a is not "идите подальше со своими тестами")


print(*roundrobin('abc', 'd', 'ef'))


numbers = [1, 2, 3]
letters = iter('beegeek')

print(*roundrobin(numbers, letters))

print(list(roundrobin()))

numbers = iter([1, 2, 3])
nones = iter([None, None, None, None])

print(*roundrobin(numbers, nones))