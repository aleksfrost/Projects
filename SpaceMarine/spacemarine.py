'''
Дневник космонавта 🌶️
Вам доступен текстовый файл diary.txt, в который космонавт записывал
небольшие отчёты за день. Каждый новый отчёт он мог записать либо в начало файла,
либо в середину, либо в конец. Все отчеты разделены между собой пустой строкой.
Каждый новый отчёт начинается со строки с датой и временем в формате DD.MM.YYYY; HH:MM,
после которой следуют события, произошедшие за указанный день:
'''


from datetime import datetime

data = []
temp = []
with open('diary.txt', encoding='utf-8') as file:
    for line in file:
        if len(line) != 0:
            while len(line.strip()) != 0:
                temp.append(line.strip())
                line = file.readline()
            data.append(temp)
            temp = []

for i in range(len(data)):
    d, m, y, H, M = data[i][0].split('; ')[0].split('.') + data[i][0].split('; ')[1].split(':')
    temp_date = datetime(int(y), int(m), int(d), int(H), int(M))
    data[i][0] = temp_date

data.sort(key=lambda x: x[0])

for i in range(len(data)):
    print(data[i][0].strftime('%d.%m.%Y; %H:%M'))
    for b in data[i][1:]:
        print(b)
    if i != (len(data) - 1):
        print()

