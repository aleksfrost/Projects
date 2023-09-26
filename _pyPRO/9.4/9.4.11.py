def numbers_sum(elems):
    """Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет."""

    res = 0
    for elem in elems:
        if isinstance(elem, int):
            res += int(elem)
        elif isinstance(elem, float):
            res += float(elem)

    return res



print(numbers_sum([1, '2', 3, 4, 'five']))
print(numbers_sum(['beegeek', 'stepik', '100']))
print(numbers_sum.__doc__)