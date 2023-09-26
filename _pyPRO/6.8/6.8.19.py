from collections import Counter


def scrabble(symbols, word):
    w = Counter(word.lower())
    s = Counter(symbols.lower())
    return [False, True][w <= s]


print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
print(scrabble('begk', 'beegeek'))
print(scrabble('beegeek', 'beegeek'))