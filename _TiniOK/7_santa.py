n = int(input())
line = [int(i) for i in input().split(' ')]
line2 = [i for i in range(1, n + 1)]
for i in range(1, n + 1):
    if i in line and i in line2:
        line.remove(i)
        line2.remove(i)
if len(line2) == 1:
    print(line[0], line2[0])
else:
    print(-1, -1)


