import functools


def takes(*args_types):
    def takes_deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res_pos = all([type(arg) in args_types for arg in args])
            res_named = all([type(kwargs[key]) in args_types for key in kwargs])
            if res_pos and res_named:
                return func(*args, **kwargs)
            else:
                raise TypeError
        return wrapper
    return takes_deco


@takes(int, str)
def repeat_string(string, times):
    return string * times

print(repeat_string('bee', 3))


@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times

try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))

