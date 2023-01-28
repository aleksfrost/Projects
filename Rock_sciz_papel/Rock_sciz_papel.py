
rusl, tim = input(), input()

hands = ['Спок', 'ножницы', 'бумага', 'камень', 'ящерица']
winner = ['ничья', 'Руслан', 'Тимур', 'Руслан', 'Тимур']
print(winner[hands.index(tim) - hands.index(rusl)])
