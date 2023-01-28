n = int(input())
mult = [[int(ch) for ch in input().split()] for _ in range(n)]
for i in range(n):
    mult[i][i], mult[n - 1 - i][i] = mult[n - 1 - i][i], mult[i][i]
for _ in range(n):
    print(*mult[_])

