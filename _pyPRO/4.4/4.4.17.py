import json
import pprint

with open('../food_services.json', encoding='utf-8') as file:
    data_in = json.load(file)
    res_type = {}
    for obj in data_in:
        res_type.setdefault(obj['TypeObject'], []).append([obj['Name'], obj['SeatsCount']])
    res = sorted(res_type.items(), key=lambda x: x[0])
    for_out = []
    for tup in res:
        for_out.append([tup[0], sorted(tup[1], key=lambda x: int(x[1]))[-1]])
    for line in for_out:
        print(f'{line[0]}: {line[1][0]}, {line[1][1]}')
