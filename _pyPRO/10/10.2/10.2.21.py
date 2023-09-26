def transpose(matrix: list):
    iters = [iter(x) for x in matrix]
    return [list(x) for x in zip(*iters)]
    # transpose = lambda matrix: list(map(list, zip(*matrix)))

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for row in transpose(matrix):
    print(row)

matrix = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10]]

for row in transpose(matrix):
    print(row)