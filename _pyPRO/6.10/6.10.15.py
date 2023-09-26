from collections import ChainMap
from typing import Any


def get_value(chainmap: ChainMap, key, from_left: bool = True) -> Any:
    if from_left:
        for ch_map in chainmap.maps:
            if key in ch_map:
                return ch_map[key]
        return None
    for ch_map in chainmap.maps[::-1]:
        if key in ch_map:
            return ch_map[key]
    return None


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name'))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'name', False))

chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})

print(get_value(chainmap, 'age'))