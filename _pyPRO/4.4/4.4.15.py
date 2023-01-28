import csv
import pprint
from datetime import datetime
import json

with open('../exam_results.csv', encoding='utf-8') as file_in, open('../best_scores.json', 'w', encoding='utf-8', newline='') as file_out:
    pattern = '%Y-%m-%d %H:%M:%S'
    data = [line for line in csv.reader(file_in, delimiter=',')]
    head = data.pop(0)
    sort_data = {}
    for line in data:
        sort_data.setdefault(tuple([line[0], line[1], line[4]]), {}).update({datetime.strptime(line[3], pattern): int(line[2])})
#    pprint.pprint(sort_data)
    for keys in sort_data:
        sort_data[keys] = sorted(sort_data[keys].items(), key = lambda x: (x[1], x[0]))[-1]
    data_for_out = sorted(sort_data.items(), key=lambda x: x[0][2])
    out_data = [{'name': pair[0][0], 'surname': pair[0][1], 'best_score': pair[1][1],
                 'date_and_time': datetime.strftime(pair[1][0], pattern), 'email': pair[0][2]}
                for pair in data_for_out]
    json.dump(out_data, file_out, indent='   ')
