from collections import Counter


data = sorted(Counter([len(x) for x in input().split()]).items(), key=lambda x: x[1])
for d in data:
    print(f'Слов длины {d[0]}: {d[1]}')

