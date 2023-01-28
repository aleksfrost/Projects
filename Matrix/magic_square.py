# put your python code here
n = int(input())
mult = [[int(ch) for ch in input().split()] for _ in range(n)]
# Проверка на повторяемость
num_set = []
flag = True
count = 0
[num_set.extend(set(mult[_])) for _ in range(n)]
final_set = [ch for ch in set(num_set)]
for i in range(len(final_set)):
    for j in range(n):
        count += mult[j].count(int(final_set[i]))
        if count > 1:
            flag = False
            break
    count = 0
    if not flag:
        break
if 0 in final_set:
    flag = False
temp = sum(mult[0])
main_diag, sec_diag, row_sum = 0, 0, 0
if flag:
    for i in range(n):
        # Строка
        if sum(mult[i]) != temp:
            flag = False
            break
        # Сумма главной диаганали
        main_diag += mult[i][i]
        # Сумма второй диаганали
        sec_diag += mult[i][n - i - 1]
        for j in range(n):
            row_sum += mult[j][i]
        # Проверка ряда
        if row_sum != temp:
            flag = False
        row_sum = 0
    # Проверка главной диаганали
    if main_diag != temp:
            flag = False
    # Проверка второй диаганали
    if sec_diag != temp:
            flag = False
if flag:
    print('YES')
else:
    print('NO')
