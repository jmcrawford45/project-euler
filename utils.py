from functools import lru_cache
from math import ceil, sqrt
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

def primes_in_range(low: int, high: int) -> list[int]:
    sieve = [0,0] + list(range(2, high))
    out = []
    for i in sieve:
        if i == 0:
            continue
        else:
            for multiple in range(i, high, i):
                sieve[multiple] = 0
            if i >= low:
                out.append(i)
    return out

def gcd(x,y):
    while x!=y:
        if x > y:
            x -= y
        else:
            y -= x
    return x

def num_divisors(n: int) -> int:
    return len(num_divisors(n))

def divisors(n: int) -> set[int]:
    divisors = set()
    for i in range(1, ceil(sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n / i)
    return divisors
    