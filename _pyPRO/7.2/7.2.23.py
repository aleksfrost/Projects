import sys

reader = sys.stdin
res_num = 0
res_not_num = 0
for item in reader.readlines():
    try:
        res_num += float(item)
    except ValueError:
        res_not_num += 1

print(res_num if res_num % 1 else int(res_num))
print(res_not_num)
