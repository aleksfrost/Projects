import pprint
from zipfile import ZipFile

with ZipFile('workbook.zip') as file:
    data = file.infolist()
    res = {}
    for inst in data:
        if not inst.is_dir():
            res[inst.filename.split('/', -1)[-1]] = inst.compress_size * 100 / inst.file_size
    res_f = list(sorted(res.items(), key=lambda x: float(x[1])))[0]
    pprint.pprint(res_f[0])


