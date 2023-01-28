import pprint
from collections import namedtuple
import pickle

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', 'rb') as file:
    obj = pickle.load(file)
#    pprint.pprint(obj)
    i = len(obj)
    for item in obj:
        i -= 1
        for field, value in zip(Animal._fields, item):
            print(f'{field}: {value}')
        if i:
            print()

