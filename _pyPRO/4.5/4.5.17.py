import pprint
from zipfile import ZipFile
from datetime import datetime
with ZipFile('workbook.zip') as file:
    data = file.infolist()
    res = []
    for inst in data:
        if not inst.is_dir():
            if '/' in inst.filename:
                res.append([inst.filename.split('/', -1)[1],
                            datetime.strptime(str(inst.date_time), '(%Y, %m, %d, %H, %M, %S)'),
                            inst.file_size,
                            inst.compress_size])
            else:
                res.append([inst.filename,
                            datetime.strptime(str(inst.date_time), '(%Y, %m, %d, %H, %M, %S)'),
                            inst.file_size,
                            inst.compress_size])
    res.sort(key=lambda x: x[0])
    print(*res, sep='\n')
