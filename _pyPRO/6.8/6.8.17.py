from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')

data.min_values = lambda: list(filter(lambda x: x[1] == min(data.values()), data.items()))
data.max_values = lambda: list(filter(lambda x: x[1] == max(data.values()), data.items()))

print(data.min_values())
print(data.max_values())