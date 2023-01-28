row = [ch for ch in input().split()]
n = len(row)
res = [[]]
j = 0
for i in range(n):
    for j in range(n):
        if len(row[j:i + j + 1]) == i + 1:
            res.append(row[j:i + j + 1])
print(res)
'''
row[0, 1, 2, 3]
row[0:1]    1 со сдвигом          0:n-3
row[1:2]                          1:n-2
row[2:3]                          2:n-1
row[3:]                           3:n
                                  
row[0:2]    2 со сдвигом          0:n-2
row[1:3]                          1:n-1
row[2:]                           2:n
                                  
row[0:3]    3 со сдвигом          0:n-1
row[1:]                           1:n
row[:]      4                     0:n
'''