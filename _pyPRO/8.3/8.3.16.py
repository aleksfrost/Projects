num_bin = []

def to_binary(num):
    if num == 1 or num == 0:
        num_bin.append(str(num))
        res = "".join(num_bin[::-1])
        num_bin.clear()
        return res
    else:
        num_bin.append(str(num % 2))
        return to_binary(num // 2)


print(to_binary(15))
print(to_binary(0))
print(to_binary(1))
print(to_binary(256))
