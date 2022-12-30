from math import *
from collections import defaultdict
from functools import lru_cache

@lru_cache(maxsize=None)
def divisors(n: int) -> set[int]:
    divisors = set()
    for i in range(1, ceil(sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors - {n}

@lru_cache(maxsize=None)
def chain_len(n: int) -> int:
    return len(chain(n))

@lru_cache(maxsize=None)
def chain(n: int) -> set[int]:
    seen = set()
    curr = n
    while curr not in seen:
        if curr > 1_000_000:
            return set()
        seen.add(curr)
        curr = sum(divisors(curr))
    return seen
max_len = 0
assert chain(12496) == set([12496, 14288, 15472, 14536, 14264])
res = set()
for i in range(2, 1_000_000):
    if i % 10_000 == 0:
        print('10k')
    if chain_len(i) > max_len:
        max_len = chain_len(i)
        res = chain(i)
print(min(res))
