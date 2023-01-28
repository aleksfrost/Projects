row = [ch for ch in input().split(' ')]
res = [[(row.pop(0))]]
i, j = 0, 0
while len(row) > 0:
    temp = row.pop(0)
    if res[i][j] == temp:
        res[i].extend([temp])
    else:
        res.append([temp])
        i += 1
print(res)