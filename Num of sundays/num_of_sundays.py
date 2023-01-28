from datetime import date


def num_of_sundays(year):
    current = date(year, month=1, day=1).toordinal()
    finish = date(year + 1, month=1, day=1).toordinal()
    count = 0
    for num in range(current, finish):
        if date.fromordinal(num).weekday() == 6:
            count += 1
    return count


print(num_of_sundays(2021))


year = 2000
print(num_of_sundays(year))


print(num_of_sundays(768))
