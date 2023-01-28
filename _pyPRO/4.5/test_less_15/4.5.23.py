import pprint
from zipfile import ZipFile

from pathlib import Path

# prefix components:
space =  '  '
branch = ''
# pointers:
tee =    ''
last =   ''


def tree(dir_path: Path, prefix: str=''):
    """A recursive generator, given a directory Path object
    will yield a visual tree structure line by line
    with each line prefixed by the same characters
    """
    contents = list(dir_path.iterdir())
    # contents each get pointers that are ├── with a final └── :
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        yield prefix + pointer + path.name
        if path.is_dir(): # extend the prefix and recurse:
            extension = branch if pointer == tee else space
            # i.e. space because last, └── , above so no more |
            yield from tree(path, prefix=prefix+extension)


with ZipFile('desktop.zip') as file:
    data = file.infolist()
    res = []
    dict_res = {}
    dict_dict_res = {}
    for inst in data:
        res.append(inst.filename.split('/'))
    pprint.pprint(sorted(res, key=lambda x: (len(x), x)))

for line in tree(Path.home() / 'pyscratch'):
    print(line)

    Приведенный
    ниже
    код:


    def append(element, seq=[]):
        seq.append(element)
        return seq


    print(append(10))
    print(append(5))
    print(append(1))
    print(append(3))
    выводит:

    [10]
    [10, 5]
    [10, 5, 1]
    [10, 5, 1, 3]