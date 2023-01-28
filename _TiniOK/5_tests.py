# read boundaries
low, high = [int(i) for i in input().split()]

max_low = len(str(low))*str(max([int(i) for i in str(low)]))
res = []
print(max_low)

fin = max_low
while fin < high:
    res.append(max_low)
