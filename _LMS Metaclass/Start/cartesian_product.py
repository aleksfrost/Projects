def cartesian_product(arr1, arr2):
    res = []
    for i in arr1:
        for j in arr2:
            res.append((i, j))
    return res


print(cartesian_product([1, 2], [3, 4]))
"""
cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
"""