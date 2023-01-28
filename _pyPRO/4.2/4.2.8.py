import csv

with open('../titanic.csv', encoding='utf-8') as file:
    res = []
    data = [row for row in csv.reader(file, delimiter=';') if row[-1] != 'age' and int(row[0]) == 1 and float(row[-1]) < 18 ]
    for d in data:
        if d[2] == 'male':
            res.append(d[1])
    for d in data:
        if d[2] == 'female':
            res.append(d[1])

    for row in res:
        print(row)