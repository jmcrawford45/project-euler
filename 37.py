digits = list(range(1, 10))
from math import *
from functools import lru_cache

@lru_cache
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def truncatable_prime(n: int) -> bool:  
    return all(is_prime(int(str(n)[:i+1])) and is_prime(int(str(n)[i:])) for i in range(len(str(n))))
assert truncatable_prime(3797)
assert not truncatable_prime(43)
primes = [d for d in digits if is_prime(d)]
res = []
curr = 10
while len(res) < 11:
    if truncatable_prime(curr):
        res.append(curr)
    curr += 1
print(sum(res))
    

