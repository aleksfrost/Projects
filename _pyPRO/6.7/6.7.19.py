import string
from collections import Counter


with open('pythonzen.txt', encoding='utf-8') as file:
    data_clear = [d.lower() for d in file.read() if d in string.ascii_letters]
    res = sorted(Counter(data_clear).items(), key=lambda x: x[0])

for letter in res:
    print(f'{letter[0]}: {letter[1]}')

