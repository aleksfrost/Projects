from collections import defaultdict


def flip_kv_vk_safe(coll):
    res = defaultdict(list)
    for item in coll.items():
        res[item[1]].append(item[0])
    return dict(res.items())


print(flip_kv_vk_safe({
    'Санкт-Петербург': '+3',
    'Москва': '+3',
}))

""""
flip_kv_vk_safe({
    'Санкт-Петербург': '+3',
    'Москва': '+3',
}) == {
    '+3': ['Москва', 'Санкт-Петербург'],
}
"""