import copy


def card_deck(suit):
    card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз"]

    card_mast = ["пик", "треф", "бубен", "червей"]

    while True:
        new_mast = copy.copy(card_mast)
        new_mast.remove(suit)
        for mast in new_mast:
            for value in card_values:
                yield " ".join([value, mast])
        card_deck(suit)


generator = card_deck('пик')

print(next(generator))
print(next(generator))
print(next(generator))


generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]

print(*cards)


