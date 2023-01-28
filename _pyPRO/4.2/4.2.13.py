import csv

with open('../prices.csv', encoding='utf-8') as file_in:
    data = [row for row in csv.reader(file_in, delimiter=';')]
#    print(*data, sep='\n')
    min_line = []
    minimums = {}
    for line in data[1:]:
        minimums[line[0]] = list([])
        temp = min(line[1:], key=int)
        for i in range(len(line) - 1):
            if line[i + 1] == temp:
                minimums[line[0]].append([data[0][i+1], temp])
#    print(*minimums.items(), sep='\n')
    minimum = sorted(minimums.items(), key=lambda x: (int(x[1][0][1]), x[1][0][0], x[0]))
#    print('SEP-SEP-SEP-SEP-SEP-SEP-SEP-SEP-SEP-SEP-SEP-SEP-SEP')
#    print(*minimum, sep='\n')
    print(f'{minimum[0][1][0][0]}: {minimum[0][0]}')



