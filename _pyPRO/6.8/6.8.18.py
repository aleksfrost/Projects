import csv
from collections import Counter

with open('name_log.csv', encoding='utf-8') as file:
    data = [line[1] for line in csv.reader(file)][1:]

res = sorted(Counter(data).items(), key=lambda x: x[0])
for r in res:
    print(f'{r[0]}: {r[1]}')
