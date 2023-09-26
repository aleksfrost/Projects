import csv
import json

from collections import Counter

data = []
for f in ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']:
    with open(f, encoding='utf-8') as file:
        data.extend([line for line in csv.reader(file)][1:])

with open('prices.json', encoding='utf-8') as file:
    prices = json.load(file)

res = Counter()

for d in data:
    res.update([d[0]]*sum([int(k) for k in d[1:]]))

total = sum(map(lambda x: x[1] * prices[x[0]], res.items()))

print(total)

