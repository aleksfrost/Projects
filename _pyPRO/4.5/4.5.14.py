from zipfile import ZipFile

with ZipFile('workbook.zip') as file:
    data = file.infolist()
    res = sum(map(lambda x: not x.is_dir(), data))
    print(res)
