import json
import sys

string = sys.stdin.read()

s_json = json.loads(string)
for item in s_json.items():
    if not isinstance(item[1], list):
        print(*item, sep=': ')
    else:
        print(item[0], ', '.join([str(x) for x in item[1]]), sep=': ')

"""
is_correct_json('{"size": 36, "style": "bold", "name": "text1", "alignment": "center"}')
is_correct_json('''{
 "type": "donut", 
 "name": "Cake", 
 "tastes": ["chocolate", "cream", "strawberry"]
}''')

ctrl+D в конце
"""