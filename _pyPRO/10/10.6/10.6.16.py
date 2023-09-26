def is_prime(number):
    res = [k for k in range(2, number // 2 + 1) if number % k == 0]
    if len(res) > 1 or number == 1:
        return False
    else:
        return True


print(is_prime(7))

print(is_prime(8))

print(is_prime(1))