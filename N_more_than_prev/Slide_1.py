row = input().split(' ')
new_row = [row[len(row) - 1]]
for i in range(0, len(row) - 1):
    new_row.append(row[i])
print(*new_row)
