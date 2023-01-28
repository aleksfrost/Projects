import csv


def mid_arith(tup):
    return sum(tup[1]) / len(tup[1])


with open('../salary_data.csv', encoding='utf-8') as csv_in:
    csv_row = [row for row in csv.reader(csv_in, delimiter=';')]
    skip_header = csv_row.pop(0)
    data_dict = {}
    csv_row.sort()
    for row in csv_row:
        data_dict[row[0]] = data_dict.get(row[0], list()) + [int(row[1])]

    res = sorted(data_dict.items(), key=lambda x: mid_arith(x))
    for d in res:
        print(d[0])

