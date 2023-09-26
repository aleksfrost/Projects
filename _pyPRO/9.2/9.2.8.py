def hash_as_key(objects):
    res = {}
    for obj in objects:
        if not res.get(hash(obj)):
            res[hash(obj)] = obj
        else:
            if isinstance(res[hash(obj)], list):
                res[hash(obj)].append(obj)
            else:
                res[hash(obj)] = [res[hash(obj)], obj]
    return res


data = [1, 2, 3, 4, 5, 5]

print(hash_as_key(data))

data = [-1, -2, -3, -4, -5]

print(hash_as_key(data))

data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

print(hash_as_key(data))

data = [5, 5, 5]

print(hash_as_key(data))