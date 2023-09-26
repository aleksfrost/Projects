def get_id(names, name) -> int:
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    elif not name.istitle() or not name.isalpha():
        raise ValueError('Имя не является корректным')
    else:
        names.append(name)
        next_id = len(names)
        return next_id


names = ['Timur', 'Anri', 'Dima']
name = 'Arthur'

print(get_id(names, name))

names = ['Timur', 'Anri', 'Dima', 'Arthur']
name = 'Ruslan1337'

try:
    print(get_id(names, name))
except ValueError as e:
    print(e)

names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = ['E', 'd', 'u', 'a', 'r', 'd']

try:
    print(get_id(names, name))
except TypeError as e:
    print(e)