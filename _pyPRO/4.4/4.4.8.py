import json

with open('../data1.json', encoding='utf-8') as file1, open('../data2.json', encoding='utf-8') as file2, \
        open('../data_merge.json', 'w', encoding='utf-8') as out:
    data1 = json.load(file1)
    data2 = json.load(file2)
#    print(data1, data2, sep='\n')
    merge_out = {}
    merge_out.update(data1)
    merge_out.update(data2)
    json.dump(merge_out, out, indent='   ')
