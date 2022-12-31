from functools import lru_cache
from math import *
@lru_cache(maxsize=None)
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = [p for p in range(100) if is_prime(p)]

@lru_cache(maxsize=None)
def combos(amount: int, max_usable=primes[-1]) -> int:
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    return sum(combos(amount-coin, coin) for coin in primes if coin <= max_usable)
res = 0
for i in range(2, 100):
    if combos(i) > 5000:
        print(i)
        break
    res = max(combos(i), res)