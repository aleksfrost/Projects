
row = [int(input()) for _ in range(int(input()))]

res = int(input())

flag = 'НЕТ'

for i in range(len(row)):
    temp = row[i]
    for j in range(len(row)):
        if i == j:
            continue
        else:
            if res == row[i] * row[j]:
                flag = 'ДА'
print(flag)
