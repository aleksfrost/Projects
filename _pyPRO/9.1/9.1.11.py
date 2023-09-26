def custom_isinstance(objects, typeinfo):
    count = 0
    for object in objects:
        if isinstance(typeinfo, tuple):
            for typeinf in typeinfo:
                if isinstance(object, typeinf):
                    count += 1
        else:
            if isinstance(object, typeinfo):
                count += 1
    return count


numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, int))

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, (int, float)))

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, list))