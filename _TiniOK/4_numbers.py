# read cont numbers and count changes
count, changes = [int(i) for i in input().split()]

# read numbers
numbers = [int(i) for i in input().split()]


# num to list of ints
def num_to_ciphers(num):
    return [int(i) for i in str(num)]


# number to dict of '10**i'
def list_to_tens(row):
    return {str(10**i): k for i, k in zip(range(len(row)), row[::-1])}


# all numbers to dicts
res = []
for n in numbers:
    res.append(list_to_tens(num_to_ciphers(n)))

# all numbers to list of gains
res1 = []
for obj in res:
    for key in obj:
        res1.append(int(key)*(9-obj[key]))
# get max's for count of changes
print(sum(sorted(res1, key=int, reverse=True)[:changes]))
