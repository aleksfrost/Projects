from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе', 'AdmArea': 'Центральный административный округ', 'District': 'район Арбат', 'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

new_data = OrderedDict()

for i in range(len(data)):
    if i % 2:
        temp = data.popitem()
        new_data[temp[0]] = temp[1]
    else:
        temp = data.popitem(last=False)
        new_data[temp[0]] = temp[1]

print(new_data)
