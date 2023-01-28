import json
from zipfile import ZipFile


with ZipFile('data.zip') as file:
    file.extractall('data')
    data = file.infolist()
    res = []
    for inst in data:
        if not inst.is_dir() and inst.filename.split('.')[-1] == 'json':
            with open('data/' + inst.filename, encoding='utf-8') as j_file:
                try:
                    data = json.load(j_file)
                    res.append(data)
                except ValueError:
                    pass
    to_out = list(filter(lambda x: 'Arsenal' in x['team'], sorted(res, key=lambda x: [x['first_name'], x['last_name']])))
    for obj in to_out:
        print(obj['first_name'], obj['last_name'])
