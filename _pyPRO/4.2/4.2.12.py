import csv

with open('../student_counts.csv', encoding='utf-8') as file_in, open('../sorted_student_counts.csv', 'w',
                                                                      encoding='utf-8', newline='') as file_out:
    data = [row for row in csv.reader(file_in, delimiter=',')]
#    print(*data, sep='\n')
    n = len(data[0])
    m = len(data)
    print(f'n{n}, m{m}')
    trans_data = []
    for i in range(n):
        trans_data.append([data[j][i] for j in range(m)])
    print(*trans_data, sep='\n')
    head = trans_data.pop(0)
    new_data = sorted(trans_data, key=lambda x: (int(x[0].split('-')[0]), x[0].split('-')[1]))
    new_data.insert(0, head)
    print(*new_data, sep='\n')
    n = len(new_data[0])
    m = len(new_data)
    trans_new_data = []
    for i in range(n):
        trans_new_data.append([new_data[j][i] for j in range(m)])
    print(*trans_new_data, sep='\n')
    writer = csv.writer(file_out)
    for row in trans_new_data:
        writer.writerow(row)
