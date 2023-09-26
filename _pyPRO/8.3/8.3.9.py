def range_sum(arr: list, x: int, y: int) -> int:
    if x == y:
        return arr[x]
    else:
        return arr[x] + range_sum(arr, x+1, y)


print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, 7))
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8))
print(range_sum([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 0))
