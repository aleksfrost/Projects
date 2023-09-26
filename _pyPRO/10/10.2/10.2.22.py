def get_min_max(data: list):
    if not data:
        return None
    return data.index(min(data)), data.index(max(data))

data = [2, 3, 8, 1, 7]

print(get_min_max(data))


data = [1, 1, 2, 3, 8, 8]

print(get_min_max(data))


data = [9]

print(get_min_max(data))

data = []

print(get_min_max(data))