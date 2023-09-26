def get_all_values(nested_dicts, key):
    res = set()
    if key in nested_dicts:
        res.add(nested_dicts[key])  # базовый случай

    for k, v in nested_dicts.items():
        if isinstance(v, dict):
            res.update(get_all_values(v, key))  # рекурсивный случай
    return res


my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur': {'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')

print(*sorted(result))

my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'hobby')

print(*sorted(result))

my_dict = {'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 'Timur': {'hobby': 'math'}}
result = get_all_values(my_dict, 'top_grade')

print(len(sorted(result)))
