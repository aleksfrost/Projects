# Перевод чисел из десятичной системы счисления в 2, 8, 16
num = int(input())


def boh(n):
    print(bin(n)[2:])
    print(oct(n)[2:])
    print(hex(n).upper()[2:])


boh(num)
