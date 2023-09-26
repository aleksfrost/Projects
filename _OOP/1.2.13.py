class Empty:
    pass


my_list = [
    ('apple', 23),
    ('banana', 80),
    ('cherry', 13),
    ('date', 10),
    ('elderberry', 4),
    ('fig', 65),
    ('grape', 5),
    ('honeydew', 7),
    ('kiwi', 1),
    ('lemon', 10),
]

for tup in my_list:
    setattr(Empty, tup[0], tup[1])

print(Empty.__dict__)