def filter_names(names, ignore_char: str, max_names):
    filter_capital = (name for name in names if name[0] != ignore_char.lower() and name[0] != ignore_char.upper())
    filter_digit = (name for name in filter_capital
                    if not any(ch.isdigit() for ch in name)
                    )
    res = (a for a, _ in zip(filter_digit, range(max_names)))
    return res


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 'D', 3))

data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']

print(*filter_names(data, 't', 20))


data = ['Di6ma', 'Ti4mur', 'Ar5thur', 'Anri7620', 'Ar3453ina', '345German', 'Ruslan543', 'Soslanfsdf123', 'Geo000000r']

print(*filter_names(data, 'A', 100))