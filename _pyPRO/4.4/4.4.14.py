import json
from datetime import time, datetime

with open('../pools.json', encoding='utf-8') as file_in:
    pattern = '%H:%M'
    request = [time(hour=10), time(hour=12)]
    data = json.load(file_in)
    half_rel_data = list(filter(lambda obj: 'Понедельник' in obj['WorkingHoursSummer'] and datetime.strptime(obj['WorkingHoursSummer']['Понедельник'].split('-')[0], pattern).time() <= request[0] and datetime.strptime(obj['WorkingHoursSummer']['Понедельник'].split('-')[1], pattern).time() >= request[1], data))
    rel_data = sorted(half_rel_data, key=lambda x: (x['DimensionsSummer']['Length'], x['DimensionsSummer']['Width']))
    print(f'{rel_data[-1]["DimensionsSummer"]["Length"]}x{rel_data[-1]["DimensionsSummer"]["Width"]}')
    print(f'{rel_data[-1]["Address"]}')
