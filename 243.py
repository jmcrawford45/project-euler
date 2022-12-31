from functools import lru_cache

@lru_cache(maxsize=None)
def gcd(x,y):
    if x == 0:
        return y
    if y == 0:
        return x
    if x > y:
        return gcd(x%y, y)
    else:
        return gcd(x, y%x)

def resilience(d: int) -> float:
    res = 0
    for i in range(1, d):
        if gcd(d, i) == 1:
            res += 1
    return res / (d-1)

assert resilience(12) == 4/11
curr = 12
min_r = float('inf')
while True:
    r = resilience(curr)
    min_r = min(min_r, r)
    if curr % 100 == 0:
        print(f"{min_r} > {15499/94744}")
    if r < 15499/94744:
        print(curr)
        break
    curr += 1
