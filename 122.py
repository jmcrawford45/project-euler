from functools import lru_cache
from math import *
@lru_cache(maxsize=None)
def min_multiplications(n) -> int:
    if n == 0:
        return 0
    max_2pow = floor(log2(n))
    remainder = divmod(n, 2**max_2pow)
    return max_2pow
assert min_multiplications(15) == 5
print(sum(min_multiplications(k) for k in range(1, 201)))