def sort_priority(values, group):       ### CHEAT!!!!  numbers.sort(key=lambda x: (x not in group, x))
    values.sort(key=int)
    ungroup = list(group)
    ungroup.sort(key=int)
    for num in ungroup[::-1]:
        try:
            first = values.index(num)
            last = values[::-1].index(num)
            err = 0
        except ValueError:
            err = 1
        if not err:
            temp = values[first:len(values) - last]
            values.remove(num)
            values.insert(0, *temp)
    return values


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)

print(numbers)

numbers = [150, 200, 300, 1000, 50, 20000]
sort_priority(numbers, [300, 100, 200])

print(numbers)

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sort_priority(numbers, (300, 100, 200))

print(numbers)