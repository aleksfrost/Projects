def txt_to_dict():
    with open("planets.txt", "r", encoding="utf-8") as file:
        pairs = (sub.rstrip().split("\n") for sub in file.read().split("\n\n"))
        pre_dicts = (tuple(tuple(tup.split(" = ") for tup in pair)) for pair in pairs)
        dicts = (dict(tups) for tups in pre_dicts)
        yield from dicts



planets = txt_to_dict()

print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))
print(next(planets))

