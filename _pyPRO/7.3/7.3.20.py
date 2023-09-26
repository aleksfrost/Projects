from calendar import month_name


try:
    month = int(input())
    if 1 <= month <= 12:
        print(month_name[month])
    else:
        print('Введено число из недопустимого диапазона')
except ValueError:
    print('Введено некорректное значение')
