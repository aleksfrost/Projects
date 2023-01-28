import json
import pprint
import time


with open('../people.json', encoding='utf-8') as file_in, open('../update_people.json', 'w', encoding='utf-8') as file_out:
    data = json.load(file_in)
    start_time = time.perf_counter_ns()  # START
    keys = set()
    for line in data:
        for item in line.items():
            keys.add(item[0])
    for i in range(len(data)):
        for key in keys:
            if key in data[i]:
                pass
            else:
                data[i].update({key: None})

    json.dump(data, file_out, indent='   ')
    end_time = time.perf_counter_ns()  # STOP
    elapsed_time = end_time - start_time
    print(elapsed_time)

"""
start_time = time.perf_counter_ns()  # START
        g(arg)
        end_time = time.perf_counter_ns()  # STOP
        elapsed_time = end_time - start_time
        
        with all checks: 9726500
        without: 5748500
"""