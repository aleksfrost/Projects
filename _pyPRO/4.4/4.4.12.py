import json
import csv
import pprint

#import pprint

with open('../students.json', encoding='utf-8') as file_in, open('../data.csv', 'w', encoding='utf-8', newline='') as file_out:
    data = json.load(file_in)
    head = ['name', 'phone']
    to_out = [head]
    adult = 18
    grade_pass = 75
    headless = [[obj['name'], obj['phone']] for obj in data if obj['age'] >= adult and obj['progress'] >= grade_pass]
    headless.sort()
    to_out.extend(headless)
#    pprint.pprint(to_out)
    writer = csv.writer(file_out, delimiter=',')
    for line in to_out:
        writer.writerow(line)
