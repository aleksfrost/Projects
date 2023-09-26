def sand_watch(start=16, stop=4, cipher=1):
    if start > stop:
        print(f'{str(cipher)*start}'.center(16).rstrip())
        sand_watch(start-stop, cipher=cipher+1)
    print(f'{str(cipher)*start}'.center(16).rstrip())


sand_watch()

"""
def bee(n):
    if n > 0:
        print(n)
        bee(n - 1)
    print(n)

bee(2)
center(16).rstrip() ?"""