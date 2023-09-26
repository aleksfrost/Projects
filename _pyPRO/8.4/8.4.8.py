def dict_travel(nested_dicts, depth=None):
    to_do = dict(sorted(nested_dicts.items(), key=lambda x: x[0]))
    for key in to_do:
        if depth is None:
            depth = []
        path = depth + [key]
        if isinstance(nested_dicts[key], dict):
            dict_travel(nested_dicts[key], path)
        else:
            print(f"{'.'.join(path)}: {nested_dicts[key]}")





data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}

dict_travel(data)
print("TA_DAM_DAM!!!!")
data = {'d': 1, 'b': {'c': 30, 'a': 10, 'b': 20}, 'a': 100}

dict_travel(data)
print("TA_DAM_DAM!!!!")
data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}

dict_travel(data)
print("TA_DAM_DAM!!!!")