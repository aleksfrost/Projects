from datetime import date


def years_days(year):
    return (date.fromordinal(dat)
            for dat in range(date.toordinal(date(year=year, month=1, day=1)), date.toordinal(date(year=year+1, month=1, day=1)))
            )


dates = years_days(2022)

print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))


