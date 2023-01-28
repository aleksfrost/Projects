# Перевод чисел из десятичной системы счисления в любую другую
ch_n = int(input())
n = int(input())


def ten_to_10(ch_n, n):
    res = []
    alph_d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    while ch_n // n != 0:
        res.append(str(alph_d[ch_n % n]))
        ch_n //= n
    res.append(str(ch_n))
    ''.join(res)
    return res[::-1]


print(*ten_to_10(ch_n, n), sep='')
