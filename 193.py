from utils import *
from math import floor
from decimal import *
getcontext().prec = 100

def squarefree_below(n) -> int:
    """
    Create a sieve count starting with 0
    """
    primes = primes_in_range(2, ceil(n**0.5))
    n=n-1
    res = 0
    for i, p in enumerate(primes):
        portion = Decimal(n) // Decimal(p**2)
        for p2 in primes[i+1:]:
            denom = p**2 * p2**2
            if denom > n+1:
                break
            portion -= Decimal(n) // Decimal(denom)
        res += floor(portion)
        
    return n-res

def naive(n) -> int:
    primes = primes_in_range(2, ceil(n**0.5))
    res = 0
    for i in range(1, n):
        for p in primes:
            if i % p**2 == 0:
                res += 1
                break
    return n-res-1



assert squarefree_below(901) == naive(901)
# print(naive(10000), squarefree_below(10000))
# print(naive(1000), squarefree_below(1000))
assert squarefree_below(36) == naive(36)
# # print(squarefree_below(1000),naive(1000))

# print(1000-naive(1000), 1000-squarefree_below(1000))
for i in range(1, 1000):
    if squarefree_below(i) != naive(i):
        print(i, squarefree_below(i), naive(i))
assert squarefree_below(1000) == naive(1000)
print(squarefree_below(2**50-1))