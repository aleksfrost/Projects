from math import *


def get_triangle_row(row):
    return [int(get_triangle_elem(row, i)) for i in range(row + 1)]


def get_triangle_elem(row, elem):
    return factorial(row) / (factorial(elem) * factorial((row - elem)))


def get_triangle(n):
    triangle = []
    for i in range(n):
        triangle.append(get_triangle_row(i))
    return triangle


n = int(input('Введи число рядов: '))
for i in range(n):
    print(*get_triangle(n)[i])
