def get_len(n, length=0):
    if n // 10:
        length += 1
        get_len(n // 10, length)
    else:
        length += 1
        print(length)


get_len(int(input()))
