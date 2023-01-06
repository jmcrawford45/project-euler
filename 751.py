from functools import lru_cache
from math import floor

@lru_cache(maxsize=None)
def b(n: tuple[int], i):
    if i == 1:
        return int(''.join(str(i) for i in n)) / (10** len(n)-1)
    return floor(b(n, i-1)) * (b(n, i-1) - floor(b(n, i-1)) + 1)

def a(n, i):
    return floor(b(n, i))

def tau(n):
    out = []
    for i in range(1, 25):
        out.append(a(n, i))
    return out
print(tau((2,9,5,6,9,3)))
assert tau((2,))[0] == 2