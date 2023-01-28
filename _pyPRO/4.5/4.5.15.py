from zipfile import ZipFile

with ZipFile('workbook.zip') as file:
    data = file.infolist()
    res = sum(map(lambda x: x.file_size, data))
    res_compr = sum(map(lambda x: x.compress_size, data))
    print(f'Объем исходных файлов: {res} байт(а)')
    print(f'Объем сжатых файлов: {res_compr} байт(а)')
