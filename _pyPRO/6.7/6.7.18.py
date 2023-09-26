from collections import Counter

coll = Counter(input().split(','))
sorted_coll = sorted(coll.items(), key=lambda x: x[0])
max_len = len(max(sorted_coll, key=lambda x: len(x[0]))[0])
for obj in sorted_coll:
    print(f'{obj[0].ljust(max_len)}: {sum([ord(x) for x in obj[0] if x != " "])} UC x {obj[1]} = {sum([ord(x) for x in obj[0] if x != " "]) * obj[1]} UC')
