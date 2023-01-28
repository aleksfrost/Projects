from datetime import date


def is_available_date(booked_dates, date_for_booking):
    def add_dates(dates_read):
        if len(dates_read) < 15:
            day, month, year = dates_read.split('.')
            return [date(int(year), int(month), int(day))]
        else:
            interval = []
            start = dates_read.split('-')[0]
            day, month, year = start.split('.')
            start_date = date(int(year), int(month), int(day)).toordinal()
            finish = dates_read.split('-')[1]
            day, month, year = finish.split('.')
            finish_date = date(int(year), int(month), int(day)).toordinal()
            for temp in range(start_date, finish_date + 1):
                interval.append(date.fromordinal(temp))
            return interval

    booked = []
    for temp_date in booked_dates:
        booked.extend(add_dates(temp_date))

    for_book = add_dates(date_for_booking)

#    print(booked)
#    print(for_book)

    for day_for in for_book:
        if day_for in booked:
            return False
    return True


dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))