import csv

with open('../data.csv', encoding='utf-8') as file:
    data = [row[-1].split('@')[-1] for row in csv.reader(file, delimiter=',')]
    skip = data.pop(0)
    data.sort()
    data_for_out = {}
    for d in data:
        data_for_out[d] = data_for_out.setdefault(d, 0) + 1
    out_list = sorted(data_for_out.items(), key=lambda x: x[-1])

with open('../domain_usage.csv', 'w', encoding='utf-8', newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerow(['domain', 'count'])
    for row in out_list:
        writer.writerow(row)
