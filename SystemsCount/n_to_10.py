
# В саду 88_n фруктовых деревьев, из них 32_n яблони, 22_n груши, 16_n слив и 17_n вишен.
# В какой системе счисления посчитаны деревья?

def n_to_10(ch_n, n):
    res10 = 0
    alph_d = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    for i in range(len(ch_n)):
        if ch_n[i].isdigit():
            res10 += int(ch_n[i]) * n**(len(ch_n) - 1 - i)
        else:
            res10 += alph_d.index(ch_n[i]) * n ** (len(ch_n) - 1 - i)
    return int(res10)


for i in range(1, 17):
    if n_to_10('88', i) == n_to_10('32', i) + n_to_10('22', i) + n_to_10('16', i) + n_to_10('17', i):
        print(i)
        print(n_to_10('88', i))

