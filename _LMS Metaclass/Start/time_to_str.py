from datetime import timedelta


def seconds_to_str(secs):
    dt = timedelta(seconds=secs)
    d = dt.days
    h = dt.seconds // 3600
    m = dt.seconds % 3600 // 60
    s = dt.seconds % 3600
    if d:
        return f'{d:0{2}}d{h:02}h{m:02}m{s:02}s'
    elif h:
        return f'{h:02}h{m:02}m{s:02}s'
    elif m:
        return f'{m:02}m{s:02}s'
    else:
        return f'{s:02}s'


print(seconds_to_str(20))
print(seconds_to_str(60))
print(seconds_to_str(65))
print(seconds_to_str(3700))
print(seconds_to_str(93600))
