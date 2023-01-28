import json


def is_correct_json(string):
    try:
        s_json = json.loads(string)
        return True
    except ValueError:
        return False


print(is_correct_json("felghsghgohg;ohr'giha'gja'gjgbsnjb;osihg;oihajsr;goha;rhg;arhga;rh"))
print(is_correct_json('number = 17'))
data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'

print(is_correct_json(data))