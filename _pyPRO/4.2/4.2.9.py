import csv
from datetime import datetime

with open('../name_log.csv', encoding='utf-8') as file, open('../new_name_log.csv', 'w', encoding='utf-8', newline='') as out:
    data = [row for row in csv.reader(file, delimiter=',')]
    head = data.pop(0)
    new_list = {}
    pattern = '%d/%m/%Y %H:%M'
    for row in data:
        if new_list.get(row[1], 0) == 0:
            new_list[row[1]] = [row[0], row[2]]
        else:
            curr_datetime = datetime.strptime(new_list.get(row[1])[1], pattern)
            new_datetime = datetime.strptime(row[2], pattern)
            if new_datetime > curr_datetime:
                new_list[row[1]] = [row[0], row[2]]

    data_for_out_0 = sorted(new_list.items(), key=lambda x: x[0])
    data_for_out = [head]
    for row in data_for_out_0:
        data_for_out.append([row[1][0], row[0], row[1][1]])

    writer = csv.writer(out)
    for row in data_for_out:
        writer.writerow(row)

