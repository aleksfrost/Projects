obj = eval(input())
if isinstance(obj, list):
    print(obj[-1])
if isinstance(obj, tuple):
    print(obj[0])
if isinstance(obj, set):
    print(len(obj))
