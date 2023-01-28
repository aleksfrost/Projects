n = 8
stallion = [ch for ch in input()]
rows = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
desk = [['.' for _ in range(n)] for _ in range(n)]
x1, y1 = 8 - int(stallion[1]), rows.index(stallion[0])

for x2 in range(n):
    for y2 in range(n):
        if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
            desk[x2][y2] = '*'
desk[8 - int(stallion[1])][rows.index(stallion[0])] = 'Q'
for _ in range(n):
    print(*desk[_])

