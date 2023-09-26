def corresponding_pairs(arr1, arr2):
    return [tuple([x, y]) for x, y in zip(arr1, arr2)]


print(corresponding_pairs([1, 2], ['A', 'B']))
print(corresponding_pairs([1, 2], ['A', 'B', 'C']))
print(corresponding_pairs([1, 2], ['A']))
"""
corresponding_pairs([1, 2], ['A', 'B']) == [(1, 'A'), (2, 'B')]
corresponding_pairs([1, 2], ['A', 'B', 'C']) == [(1, 'A'), (2, 'B')]
corresponding_pairs([1, 2], ['A']) == [(1, 'A')]
"""