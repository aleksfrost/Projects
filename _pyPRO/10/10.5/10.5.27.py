def flatten(nested_list):
    other_list = []
    for nest in nested_list:
        if isinstance(nest, list):
            other_list.extend(flatten(nest))
        else:
            other_list.append(nest)
    yield from other_list


generator = flatten([[1, 2], [[3]], [[4], 5]])

print(*generator)


generator = flatten([1, 2, 3, 4, 5, 6, 7])

print(*generator)