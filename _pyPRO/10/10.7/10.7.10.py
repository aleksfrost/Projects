def nonempty_lines(file):
    with open(file, 'r', encoding='utf-8') as file:
        lines_all = (line.rstrip() for line in file if line.rstrip())
        yield from (line if len(line) <= 25 else "..." for line in lines_all)



lines = nonempty_lines('data2.txt')

print(next(lines))
print(next(lines))
print(next(lines))
print(next(lines))


print(*nonempty_lines('data2.txt'))