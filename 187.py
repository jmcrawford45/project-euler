from utils import *
from itertools import product
def prime_products_below(high) -> int:
    primes = primes_in_range(2,high)
    print(len(primes))
    count = 0
    for i, p1 in enumerate(primes):
        if high > 10**4 and (i % high//100) == 0:
            print(f"{i // high//100}%")
        for p2 in primes[i:]:
            if p1 * p2 < high:
                count += 1
            else:
                continue
    return count
    # return len(set(i*j for i,j in product(primes, primes) if i*j < high))
assert prime_products_below(30) == 10
print(prime_products_below(10**8))
