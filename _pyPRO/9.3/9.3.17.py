def print_operation_table(operation, rows, cols):
    res = [[str(operation(x, y)).center(5) for y in range(1, cols+1)] for x in range(1, rows+1)]
    for x in range(0, rows):
        print(*res[x])


print_operation_table(lambda a, b: a * b, 5, 5)

print_operation_table(pow, 5, 4)
