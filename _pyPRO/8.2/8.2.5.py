def count(start, stop):
    print(start)
    if start < stop:
        start += 1
        count(start, stop)


count(1, 100)
