class CardDeck:
    def __init__(self):
        self.nums = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "валет", "дама", "король", "туз")
        self.shirts = ("пик", "треф", "бубен", "червей")
        self.cards = iter([num + " " + shirt for shirt in self.shirts for num in self.nums])

    def __iter__(self):
        return self

    def __next__(self):
        next_card = next(self.cards)
        if next_card:
            return next_card
        else:
            raise StopIteration


cards = CardDeck()

print(next(cards))
print(next(cards))


cards = list(CardDeck())

print(cards[9])
print(cards[23])
print(cards[37])
print(cards[51])


