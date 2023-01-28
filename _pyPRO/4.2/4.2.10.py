import csv

col = int(input()) - 1
with open('../deniro.csv', encoding='utf-8') as file:
    data = [row for row in csv.reader(file, delimiter=',')]
    code = []
    i = 0
    for pos in data[0]:
        try:
            code.append(bool(int(pos)))
            i += 1
        except ValueError:
            code.append(0)
            i += 1
    for row in sorted(data, key= lambda x: int(x[col]) if code[col] == 1 else x[col]):
        print(*row, sep=',')
