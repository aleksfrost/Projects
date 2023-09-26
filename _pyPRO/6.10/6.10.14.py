from collections import ChainMap


def deep_update(chainmap: ChainMap, key, value) -> None:
    is_there = False
    for ch_map in chainmap.maps:
        if key in ch_map:
            ch_map[key] = value
            is_there = True
    if not is_there:
        chainmap[key] = value


chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'name', 'Dima')

print(chainmap)

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'age', 20)

print(chainmap)