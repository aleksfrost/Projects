show = print


def print(*args, **kwargs):
    to_out = [ar.upper() if isinstance(ar, str) else ar for ar in args]
    if kwargs:
        if kwargs['sep'] and kwargs['end']:
            show(*to_out, sep=kwargs['sep'].upper(), end=kwargs['end'].upper())
        elif kwargs['sep']:
            show(*to_out, sep=kwargs['sep'].upper())
        elif kwargs['end']:
            show(*to_out, end=kwargs['end'].upper())
    else:
        show(*to_out)


print('beegeek', [1, 2, 3], 4)
print('bee', 'geek', sep=' and ', end=' wow')

words = ('black', 'white', 'grey', 'black-1', 'white-1', 'python')
print(*words, sep=' to ', end=' LOVE')