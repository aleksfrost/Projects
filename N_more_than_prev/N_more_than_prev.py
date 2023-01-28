row = input().split(' ')
count = 0
for i in range(1, len(row)):
    if int(row[i]) > int(row[i - 1]):
        count += 1
print(count)
