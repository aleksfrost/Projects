import copy
n = int(input())
A = [[int(ch) for ch in input().split()] for _ in range(n)]
m = int(input())

B = copy.deepcopy(A)
C = [[0 for i in range(n)] for j in range(n)]
for _ in range(m-1):
    for i in range(n):
        for j in range(n):
            for x in range(n):
                C[i][x] += B[i][j] * A[j][x]
    B = copy.deepcopy(C)
    C = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    print(*B[i])
