
"""
если объект является строкой, в его конец добавляется восклицательный знак
если объект является числом, он увеличивается на единицу
если объект является логическое значением, он инвертируется
если объект является списком, он удваивается
если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
если объект является пустым значением (null), он не добавляется
"""

import json


def to_do(arg):
    if type(arg) == str:
        return arg + '!'
    if type(arg) == float or type(arg) == int:
        return arg + 1
    if type(arg) == bool:
        return not arg
    if type(arg) == list:
        return arg * 2
    if type(arg) == dict:
        arg.update({"newkey": None})
        return arg
    if arg is None:
        pass


with open('../data.json', encoding='utf-8') as file, open('../updated_data.json', 'w', encoding='utf-8') as out:
    data = json.load(file)
#    print(data)
    new_data = []
    for obj in data:
        temp = to_do(obj)
        if temp is not None:
            new_data.append(temp)
#    print(new_data)
    json.dump(new_data, out)
