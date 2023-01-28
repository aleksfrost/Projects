n = 8
stallion = [ch for ch in input()]
rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
desk = [['.' for _ in range(n)] for _ in range(n)]
desk[8 - int(stallion[1])][rows.index(stallion[0])] = 'N'
#for _ in range(n):
#    print(*desk[_])

# move of stallion
if 0 <= (10 - int(stallion[1])) < 8 and 0 <= (rows.index(stallion[0]) + 1) < 8:
    desk[10 - int(stallion[1])][rows.index(stallion[0]) + 1] = '*'
if 0 <= (10 - int(stallion[1])) < 8 and 0 <= (rows.index(stallion[0]) - 1) < 8:
    desk[10 - int(stallion[1])][rows.index(stallion[0]) - 1] = '*'
if 0 <= (6 - int(stallion[1])) < 8 and 0 <= (rows.index(stallion[0]) + 1) < 8:
    desk[6 - int(stallion[1])][rows.index(stallion[0]) + 1] = '*'
if 0 <= (6 - int(stallion[1])) < 8 and 0 <= (rows.index(stallion[0]) - 1) < 8:
    desk[6 - int(stallion[1])][rows.index(stallion[0]) - 1] = '*'

if 0 <= (9 - int(stallion[1])) < 8 and 0 <= (rows.index(stallion[0]) + 2) < 8:
    desk[9 - int(stallion[1])][rows.index(stallion[0]) + 2] = '*'
if 0 <= (9 - int(stallion[1])) < 8 and 0 <= (rows.index(stallion[0]) - 2) < 8:
    desk[9 - int(stallion[1])][rows.index(stallion[0]) - 2] = '*'
if 0 <= (7 - int(stallion[1])) < 8 and 0 <= (rows.index(stallion[0]) + 2) < 8:
    desk[7 - int(stallion[1])][rows.index(stallion[0]) + 2] = '*'
if 0 <= (7 - int(stallion[1])) < 8 and 0 <= (rows.index(stallion[0]) - 2) < 8:
    desk[7 - int(stallion[1])][rows.index(stallion[0]) - 2] = '*'

for _ in range(n):
    print(*desk[_])
