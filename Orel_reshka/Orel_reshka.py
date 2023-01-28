temp = input()
row = [len(ch) for ch in temp.split('О')]
if len(temp.split('Р')) != 0:
    print(max(row))
else:
    print('0')

