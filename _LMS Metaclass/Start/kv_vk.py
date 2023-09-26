def flip_kv_vk(coll):
    res = {}
    for item in coll.items():
        res[item[1]] = item[0]
    return res


collect = {
    'tokyo': 'Токио',
    'moscow': 'Москва',
}
print(flip_kv_vk(collect))

""""
flip_kv_vk({
    'tokyo': 'Токио',
    'moscow': 'Москва',
}) == {
    'Токио': 'tokyo',
    'Москва': 'moscow',
}
"""