def is_iterable(obj):
    try:
        res = iter(obj)
        return True
    except:
        return False

print(is_iterable(18731))

print(is_iterable('18731'))

objects = [(1, 13), 7.0004, [1, 2, 3]]

for obj in objects:
    print(is_iterable(obj))