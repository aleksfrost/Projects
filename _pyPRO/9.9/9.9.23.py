import sys
from functools import lru_cache


@lru_cache()
def w_lecs(word: str):
    return ''.join(sorted(list(word)))


for word in sys.stdin:
    print(w_lecs(word.strip()))


# !! EOF - ctrl-D