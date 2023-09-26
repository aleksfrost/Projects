def triangle(n):
    if n > 0:
        print('*' * n)
        n -= 1
        triangle(n)


triangle(5)