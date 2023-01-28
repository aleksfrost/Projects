import json
import pprint

with open('../countries.json', encoding='utf-8') as file_in, open('../religion.json', 'w', encoding='utf-8') as file_out:
    data = json.load(file_in)
#    pprint.pprint(data)
    religion = {}
    for obj in data:
        religion[obj['religion']] = religion.setdefault(obj['religion'], []) + [obj['country']]
#    pprint.pprint(religion)
    json.dump(religion, file_out, indent='   ')
