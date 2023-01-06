from utils import *
from collections import defaultdict

# @lru_cache(maxsize=None)
# def phi(n: int) -> int:
#     res = n
#     for p in primes:
#         if p > n:
#             break
#         if n % p == 0:
#             res -= res // p
#         while n % p == 0:
#             n //= p
#     if n > 1:
#         res -= res // n
#     return res

def reduced_fractions_below(d: int) -> int:
    phi = list(range(d+1))
    for i, v in enumerate(phi):
        if i < 2:
            continue
        if i == v:
            for j in range(i, len(phi), i):
                phi[j] //= i
                phi[j] *= i-1
    res = 0
    for i in range(2, d+1):
        if i % 10000 == 0:
            print(f"{i//10000}%")
    return sum(phi[2:])
assert reduced_fractions_below(8) == 21
print(reduced_fractions_below(1_000_000))
