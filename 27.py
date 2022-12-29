from math import *
from functools import lru_cache
@lru_cache
def is_prime(n: int) -> bool:
    if n < 1:
        return False
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
max_consecutive = 0
best_pair = (0,0)
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        curr = count_primes = 0
        while True:
            if is_prime(curr**2 + curr*a + b):
                count_primes += 1
                curr += 1
                if count_primes > max_consecutive:
                    max_consecutive = count_primes
                    best_pair = (a,b)
            else:
                break
print(best_pair[0] * best_pair[1])