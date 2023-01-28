row = input().split(' ')
for i in range(1, len(row), 2):
    row[i], row[i - 1] = row[i - 1], row[i]
print(*row)
