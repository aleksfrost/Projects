from datetime import timedelta, date


def dates(start, count=None):
    if start == date(9999, 12, 31):
        return
    dlt = timedelta(days=1)
    if count is None:
        while start <= date(9999, 12, 31):
            res = start
            yield res
            try:
                start += dlt
            except StopIteration:
                return
            except OverflowError:
                return
        return
    else:
        while count > 0 and start <= date(9999, 12, 31):
            res = start
            yield res
            count -= 1
            try:
                start += dlt
            except StopIteration:
                return
            except OverflowError:
                return







generator = dates(date(2022, 3, 8))

print(next(generator))
print(next(generator))
print(next(generator))


generator = dates(date(2022, 3, 8), 5)

print(*generator)

generator = dates(date(9999, 1, 7))

for _ in range(348):
    next(generator)

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

try:
    print(next(generator))
except StopIteration:
    print('Error')