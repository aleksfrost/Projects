import csv

filename = input()
id_name = input()

# Test data
text = '''01,Artist,Otis Taylor
01,Title,Ran So Hard the Sun Went Down
01,Time,3:52
02,Artist,Waylon Jennings
02,Title,Honky Tonk Heroes (Like Me)
02,Time,3:29
03,Artist,David Allan Coe
03,Title,Willie Waylon And Me
03,Time,3:26'''

with open('../data.csv', 'w', encoding='utf-8') as file:
    file.write(text)
###########

with open(filename, encoding='utf-8') as file_in, open('../condensed.csv', 'w', encoding='utf-8', newline='') as file_out:
    data = [[row[0], [row[1], row[2]]] for row in csv.reader(file_in, delimiter=',')]
    res_dict = {}
    for row in data:
#        print(row)
        if row[0] in res_dict:
            res_dict[row[0]].append(row[1])
        else:
            res_dict[row[0]] = [row[1]]
    data_out = []
#    print(res_dict)
    temp = []
    is_head = 0
    out_data = []
    for key in res_dict:
        data_out = [key]
        for i in range(len(res_dict[key])):
            if not is_head:
                temp.append(res_dict[key][i][0])
            data_out.append(res_dict[key][i][1])
        is_head = 1
        out_data.append(data_out)
    out_data.insert(0, [id_name] + temp)
#    print(out_data)
    writer = csv.writer(file_out)
    for row in out_data:
        writer.writerow(row)
