def printerator(func):
    def upprint(*args, **kwargs):
        to_print = [arg.upper() if isinstance(arg, str) else arg for arg in args]
        if kwargs.get('sep'):
            sep = kwargs.get('sep').upper()
        else:
            sep = " "
#        old_print(sep)
        if kwargs.get('end'):
            end = kwargs.get('end').upper()
        else:
            end = "\n"
        res = func(*to_print, sep=sep, end=end)
        return res
    return upprint


old_print = print

print = printerator(print)

print('hi', 'there', end='!')
old_print()
print('are you in trouble?')
old_print()
print(111, 222, 333, sep='xxx')


