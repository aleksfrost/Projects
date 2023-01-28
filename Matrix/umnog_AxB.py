# put your python code here
n, m = [int(ch) for ch in input().split()]
A = [[int(ch) for ch in input().split()] for _ in range(n)]
ignore = input()
m, k = [int(ch) for ch in input().split()]
B = [[int(ch) for ch in input().split()] for _ in range(m)]
C = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        for x in range(k):
            C[i][x] += A[i][j] * B[j][x]
for i in range(n):
    print(*C[i])