from utils import *

def squarefree_below(n) -> int:
    """
    Create a sieve count starting with n
    """
    res = n
    for p in primes_in_range(2, ceil(n**0.5)):
        res -= n // p**2
    return res


print(squarefree_below(12))
assert squarefree_below(12) == 8
# print(squarefree_below(2**50))