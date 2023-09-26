from typing import NoReturn


def cyclic_shift(numbers: list[int | float], step: int) -> NoReturn:
    if step > 0:
        for _ in range(step):
            temp = numbers.pop(-1)
            numbers.insert(0, temp)
    else:
        for _ in range(abs(step)):
            temp = numbers.pop(0)
            numbers.append(temp)


numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, 1)

print(numbers)

numbers = [1, 2, 3, 4, 5]
cyclic_shift(numbers, -2)

print(numbers)

annotations = cyclic_shift.__annotations__

print(annotations['return'])
print(annotations['step'])