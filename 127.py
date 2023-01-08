from utils import *
from functools import lru_cache
from itertools import product
from operator import mul
from functools import reduce
from collections import defaultdict
target = 120_000
primes = primes_in_range(2, target)

prime_factor_cache = defaultdict(set)

for p in primes:
    curr = p
    while curr < target:
        prime_factor_cache[curr].add(p)
        curr += p

def prime_factors(n: int) -> set[int]:
    return prime_factor_cache[n]

def sum_hits(target: int) -> int:
    res = 0
    count = 0
    for b in range(1,target):
        for a in range(1, min(b, target-b)):
            c = a + b

            if not (prime_factors(a) & prime_factors(b)) and not (prime_factors(b) & prime_factors(c)) and not (prime_factors(a) & prime_factors(c)):
                if reduce(mul, prime_factors(a) | prime_factors(b) | prime_factors(c), 1) < c:
                    count += 1
                    res += c
    return res
assert sum_hits(1000) == 12523
print(sum_hits(120_000))

