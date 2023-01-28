dots = []
[dots.append(input()) for _ in range(int(input()))]
count_1, count_2, count_3, count_4 = 0, 0, 0, 0
for ch in dots:
    temp = ch.split(' ')
    if '0' in temp:
        continue
    elif int(temp[0]) > 0 and int(temp[1]) > 0:
        count_1 += 1
    elif int(temp[0]) > 0 and int(temp[1]) < 0:
        count_4 += 1
    elif int(temp[0]) < 0 and int(temp[1]) > 0:
        count_2 += 1
    elif int(temp[0]) < 0 and int(temp[1]) < 0:
        count_3 += 1
print(f'Первая четверть: {count_1}')
print(f'Вторая четверть: {count_2}')
print(f'Третья четверть: {count_3}')
print(f'Четвертая четверть: {count_4}')

