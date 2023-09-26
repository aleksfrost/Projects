from collections import Counter

res = sorted(Counter(input().split(',')).items(), key=lambda x: x[0])

for r in res:
    print(f'{r[0]}: {r[1]}')
