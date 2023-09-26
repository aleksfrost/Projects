n = int(input())
line = [int(i) for i in input().split()]
even = list()
odd = list()
flag = 0
for i in range(len(line)):
    if line[i] % 2 != 1 and i % 2 != 1:
        odd.append(i+1)
    if line[i] % 2 != 0 and i % 2 != 0:
        even.append(i+1)
    if len(odd) > 1 or len(even) > 1:
        print(-1, -1)
        flag = 1
        break
if len(odd) == 1 and len(even) == 1:
    print(odd[0], even[0])
elif not flag:
    print(-1, -1)

