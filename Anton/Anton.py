row = 'anton'
fridges = []
[fridges.append(input()) for _ in range(int(input()))]
for i in range(len(fridges)):
    temp = fridges[i]
    k = 0
    while True:
        if row[k] in temp:
            temp = temp[temp.index(row[k]) + 1:]
            k += 1
            if k == len(row):
                print(i + 1, end=' ')
                break
        else:
            break
