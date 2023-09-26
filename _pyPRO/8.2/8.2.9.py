def reverse_triangle(n):
    if n > 0:
        reverse_triangle(n-1)
        print('*' * n)


reverse_triangle(5)
