"""
Даны две даты — левая и правая границы диапазона соответственно. Напишите программу,
которая из этого диапазона, включая границы, выводит, начиная с даты, у которой сумма
дня и месяца нечетная, каждую третью дату, только если она не понедельник и не четверг.
"""

from datetime import datetime

pattern = '%d.%m.%Y'
right = datetime.strptime(input(), pattern).toordinal()
left = datetime.strptime(input(), pattern).toordinal()
for d in range(right, left + 1):
    d_date = datetime.fromordinal(d)
    if (d_date.day + d_date.month) % 2 == 1:
        right = d_date.toordinal()
#        print(datetime.fromordinal(right))
        break
for dd in range(right, left + 1, 3):
    d_date = datetime.fromordinal(dd)
    if d_date.weekday() not in [0, 3]:
        print(d_date.strftime(pattern))

