from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

ingredients: ChainMap = ChainMap(bread, meat, sauce, vegetables, toppings)

order = Counter(sorted(input().split(',')))
max_len = len(max(order.keys(), key=len))
bill_len = 0
total = 0

for item in order.items():
    line = f'{item[0].ljust(max_len)} x {item[1]}'
    if len(line) > bill_len:
        bill_len = len(line)
    total += item[1] * ingredients[item[0]]
    print(f'{item[0].ljust(max_len)} x {item[1]}')
if len(f'ИТОГ: {total}р') > bill_len:
    bill_len = len(f'ИТОГ: {total}р')
print('-' * bill_len)
print(f'ИТОГ: {total}р')
