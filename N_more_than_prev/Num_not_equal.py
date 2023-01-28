row = input().split(' ')
count = 0
for i in range(1, len(row)):
    if row[i] != row[i - 1]:
        count += 1
print(count + 1)

print(len(set(row)))
