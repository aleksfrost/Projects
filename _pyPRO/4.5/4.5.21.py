from zipfile import ZipFile


def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        data = zip_file.infolist()
        if len(args) != 0:
            if zip_name == args[0]:
                zip_file.extractall()
            else:
                for d in args:
                    if d in data:
                        zip_file.extract(d.filename)


extract_this('workbook.zip', 'workbook.zip')
extract_this('workbook.zip', 'earth.jpg', 'exam.txt')
extract_this('workbook.zip')