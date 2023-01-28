# 2 to 10

ch2 = '111111'
res2_10 = 0
for i in range(6):
    res2_10 += int(ch2[i]) * 2**(5 - i)
print(res2_10)

# 16 to 10

ch16 = '1AF2'
res16_10 = 0
alph_d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
for i in range(4):
    if ch16[i].isdigit():
        res16_10 += int(ch16[i]) * 16**(3 - i)
    else:
        res16_10 += alph_d.index(ch16[i]) * 16 ** (3 - i)
print(res16_10)

# n to 10




