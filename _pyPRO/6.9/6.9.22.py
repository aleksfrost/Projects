from collections import Counter
import json

with open('zoo.json', encoding='utf-8') as file:
    data = json.load(file)


res = Counter()
for d in data:
    res += Counter(d)

print(sum(res.values()))
