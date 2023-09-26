import pprint
from collections import defaultdict


def flip_dict(dict_of_list):
    res = defaultdict(list)
    for item in dict_of_list.items():
        for clue in item[1]:
            res[clue].append(item[0])
    return res


sub_res = flip_dict({'a': [1, 2], 'b': [3, 1], 'c': [2]})

pprint.pprint(sub_res)

data = {'Arthur': ['cacao', 'tea', 'juice'], 'Timur': ['coffee', 'tea', 'juice'], 'Anri': ['juice', 'coffee']}

for key, values in flip_dict(data).items():
    print(f'{key}: {", ".join(values)}')


data = {1: ['a', 'b', 'c'], 2: ['a', 'b', 'c', 'c'], 3: ['c', 'd', 'a'], 4: ['a', 'b', 'r', 'f'], 5: ['y', 'u', 'e', 'w']}

print(flip_dict(data))