def even_odd(arr):
    return sum(filter(lambda x: x % 2 == 0, arr)) / sum(filter(lambda x: x % 2 == 1, arr))


print(round(even_odd([1, 2, 3, 4, 5]), 5))

# even_odd([1, 2, 3, 4, 5]) == 0.66667  # (2 + 4) / (1 + 3 + 5)