def is_power(num) -> bool:
    if num == 1:
        return True
    elif num < 1:
        return False
    else:
        return is_power(num/2)


print(is_power(512))
print(is_power(15))
print(is_power(1))
print(is_power(100))