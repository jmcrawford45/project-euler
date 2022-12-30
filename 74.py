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
        seen.add(curr)
        curr = sum(factorial((int(c))) for c in str(curr))
    return seen
assert chain(145) == set([145])
assert chain(871) == set([871,45361])
assert chain_len(69) == 5
res = 0
for i in range(2, 1_000_000):
    if i % 10_000 == 0:
        print('10k')
    if chain_len(i) == 60:
        res += 1
print(res)
