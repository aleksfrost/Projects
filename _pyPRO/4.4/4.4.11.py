import csv
import json
import pprint

with open('../playgrounds.csv', encoding='utf-8') as file_in, open('../addresses.json', 'w', encoding='utf-8') as file_out:
    data = [line[1:] for line in csv.reader(file_in, delimiter=';')]
    skip = data.pop(0)
    out_data = {}
    for row in data:
        out_data.setdefault(row[0], {}).setdefault(row[1], []).append(row[2])
#    pprint.pprint(out_data)
    json.dump(out_data, file_out, indent='   ', ensure_ascii=False)
