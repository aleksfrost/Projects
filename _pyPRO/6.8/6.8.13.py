from collections import Counter


count = Counter(input().lower().split()).most_common()
min_count = count[-1][1]
res = sorted(list(filter(lambda x: x[1] == min_count, count)))

print(', '.join([x[0] for x in res]))

