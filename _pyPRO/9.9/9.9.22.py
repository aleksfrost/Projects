from functools import lru_cache

@lru_cache(typed=False)
def return_this(a, b):
    return a, b

print(return_this(1, 1))
print(return_this(True, True))
print(return_this(1.0, 1.0))