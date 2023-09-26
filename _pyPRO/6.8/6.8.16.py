import sys

reader = sys.stdin
data_dict = {}
data = reader.readlines()
for d in data:
    data_dict[d.split()[0]] = int(d.split()[1].strip())

res = sorted(data_dict.items(), key=lambda x: x[1])[1]
print(res[0])


