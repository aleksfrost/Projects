with open('data (1).csv', 'r', encoding='utf-8') as file:
    file_lines = (line for line in file)
    line_values = (line.rstrip().split(',') for line in file_lines)
    file_headers = next(line_values)
    arr_a = (int(amount[1]) for amount in line_values if amount[2] == 'a')
    print(sum(arr_a))


