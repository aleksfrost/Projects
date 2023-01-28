import csv
from datetime import datetime

with open('meetings.csv', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = [line for line in reader]
    header = data.pop(0)
    pattern = '%d.%m.%Y %H:%M'
    data.sort(key=lambda x: datetime.strptime(' '.join(x[2:]), pattern))
    for d in data:
        print(f'{d[0]} {d[1]}')
