"""
Скидки
Наступил ноябрь, и во многих магазинах начались распродажи, но как многим известно, зачастую товары со скидкой оказываются дороже, чем без нее. Вам доступен файл sales.csv, который содержит данные о ценообразовании различной бытовой техники. В первом столбце записано название товара, во втором — старая цена, в третьем — новая цена со скидкой:

name;old_price;new_price
Встраиваемая посудомоечная машина De'Longhi DDW 06S;23089;31862
Вытяжка Falmec Afrodite 60/600;27694;18001
...
Напишите программу, которая выводит названия тех товаров, цена на которые уменьшилась. Товары должны быть расположены в своем исходном порядке, каждый на отдельной строке.

Примечание 1. Разделителем в файле sales.csv является точка с запятой, при этом кавычки не используются.

Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.

Примечание 3. Начальная часть ответа выглядит так:

Вытяжка Falmec Afrodite 60/600
Духовой шкаф AEG BS 5836600
Вытяжка MAUNFELD PLYM 60
...
"""

import csv
import time

with open('../sales.csv', encoding='utf-8') as csv_file:

    start_time = time.perf_counter()
    rows = [row for row in csv.reader(csv_file, delimiter=';')]
    rows.pop(0)
    for row in rows:
        if int(row[1]) > int(row[2]):
            print(row[0])
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f'Время работы программы = {elapsed_time}') # 0.22411529999226332
'''
    start_time = time.perf_counter()
    rows = csv.reader(csv_file, delimiter=';')
    for row in rows:
        try:
            if int(row[1]) > int(row[2]):
                print(row[0])
        except ValueError:
            print('хм... выкинули заголовок')
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f'Время работы программы = {elapsed_time}') # 0.5120505999657325
'''