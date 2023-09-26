def non_negative_even(numbers):
    if all(map(lambda x: x >= 0 and x % 2 == 0, numbers)):
        return True
    else:
        return False


print(non_negative_even([0, 2, 4, 8, 16]))
print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))
print(non_negative_even([0, 0, 0, 0, 0]))

"""Функция должна возвращать True, если все числа в списке 
    numbers являются четными и неотрицательными, или False 
    в противном случае."""
