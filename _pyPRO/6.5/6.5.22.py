from collections import defaultdict


def wins(pairs):
    res = defaultdict(set)
    for pair in pairs:
        res[pair[0]].add(pair[1])
    return res


result = wins([('Тимур', 'Артур'), ('Тимур', 'Дима'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))


result1 = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])

for winner, losers in sorted(result1.items()):
    print(winner, '->', *sorted(losers))
