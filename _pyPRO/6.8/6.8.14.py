from collections import Counter


count = Counter(input().lower().split()).most_common()
max_count = count[0][1]
res = sorted(list(filter(lambda x: x[1] == max_count, count)))[-1]

print(res[0])

