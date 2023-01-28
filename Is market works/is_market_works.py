from datetime import datetime, timedelta

#curr = datetime.now()
#curr_delta = timedelta(hours=curr.hour, minutes=curr.minute, seconds=curr.second)
curr = datetime.strptime(input(), '%d.%m.%Y %H:%M')
curr_delta = timedelta(seconds=(curr.time().hour*60*60 + curr.time().minute*60 + curr.time().second))
schedule = {
    'Mon': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Tue': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Wed': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Thu': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Fri': {'start': timedelta(hours=9), 'end': timedelta(hours=21)},
    'Sat': {'start': timedelta(hours=10), 'end': timedelta(hours=18)},
    'Sun': {'start': timedelta(hours=10), 'end': timedelta(hours=18)}
    }
if schedule[curr.strftime('%a')]['start'] <= curr_delta < schedule[curr.strftime('%a')]['end']:
    print((schedule[curr.strftime('%a')]['end'] - curr_delta).seconds // 60)
else:
    print('Магазин не работает')

