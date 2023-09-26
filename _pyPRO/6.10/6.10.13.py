from collections import ChainMap


def get_all_values(chainmap: ChainMap, key) -> set:
    res = set()
    for ch_map in chainmap.maps:
        if key in ch_map:
            res.add(ch_map[key])
    return res


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'name')

print(*sorted(result))


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'age')

print(result)