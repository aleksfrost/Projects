def find_shortest_longest_word(line):
    arr = line.split()
    if not arr:
        return tuple([None, None])
    else:
        return tuple([min(arr, key=len), max(arr, key=len)])


print(find_shortest_longest_word('hello there, general kenobi'))
print(find_shortest_longest_word('   ') == (None, None))
"""
find_shortest_longest_word(
    'hello there, general kenobi'
) == ('hello', 'general')
"""
