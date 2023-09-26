def get_len(n, summ=0):
    if n // 10:
        summ += n % 10
        get_len(n // 10, summ)
    else:
        summ += n
        print(summ)


get_len(int(input()))
