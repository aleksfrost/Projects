list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
temp = []
for li in list1:
    li.reverse()
    temp.append(li)
list1 = temp
print(list1)
