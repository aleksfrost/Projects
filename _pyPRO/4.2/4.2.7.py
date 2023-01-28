import csv

with open('../wifi.csv', encoding='utf-8') as file:
    data = [[row[1], row[3]] for row in csv.reader(file, delimiter=';')]
    skip = data.pop(0)
    data.sort()
    data_for_out = {}
    for d in data:
        data_for_out[d[0]] = data_for_out.setdefault(d[0], 0) + int(d[1])
    out_list = sorted(data_for_out.items(), key=lambda x: x[-1], reverse=True)

    for row in out_list:
        print(f'{row[0]}: {row[1]}')
