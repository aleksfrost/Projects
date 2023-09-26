def convert(number):
    a = format(number, 'b').upper()
    b = format(number, 'o').upper()
    c = format(number, 'x').upper()
    res = [a, b, c]
    return tuple(res)


print(convert(15))
print(convert(-24))
print(convert(1))
