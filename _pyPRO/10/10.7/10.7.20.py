def stop_on(iterable, obj):
    for i in iter(iterable):
        if i == obj:
            break
        yield i

numbers = [1, 2, 3, 4, 5]

print(*stop_on(numbers, 4))


iterator = iter('beegeek')

print(*stop_on(iterator, 'a'))