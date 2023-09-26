from collections import Counter

books = Counter(input().split())
buyers = int(input())
offers = [input().split() for _ in range(buyers)]
total = 0

for item in offers:
    if books[item[0]] >= 1:
        books[item[0]] -= 1
        total += int(item[1])

print(total)

