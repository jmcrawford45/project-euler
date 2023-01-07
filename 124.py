from utils import *
from operator import mul
from functools import reduce
primes = primes_in_range(2, 100_000)

def prime_factors(n: int) -> set[int]:
    out = set()
    while n != 1:
        if is_prime(n):
            out.add(n)
            break
        for i in range(2, ceil(sqrt(n)) + 1):
            if n % i == 0:
                n = n//i
                if is_prime(i):
                    out.add(i)
                break
    return out if out else set([n])

def rad(n):
    return reduce(mul, prime_factors(n), 1)

res = []
for i in range(1, 100_001):
    res.append((rad(i), i))
res.sort()
print(res[10000-1])