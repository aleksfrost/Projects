from collections import defaultdict

data = [('Books', 1343), ('Books', 1166), ('Merch', 616), ('Courses', 966), ('Merch', 1145), ('Courses', 1061), ('Books', 848), ('Courses', 964), ('Tutorials', 832), ('Merch', 642), ('Books', 815), ('Tutorials', 1041), ('Books', 1218), ('Tutorials', 880), ('Books', 1003), ('Merch', 951), ('Books', 920), ('Merch', 729), ('Tutorials', 977), ('Books', 656)]

res = defaultdict(int)
for tup in data:
    res[tup[0]] += tup[1]
to_out = sorted(res.items(), key=lambda x: x[0])
for out in to_out:
    print(f'{out[0]}: ${out[1]}')
