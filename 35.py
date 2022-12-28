from math import *
def is_prime(n: int) -> bool:
    if n == 2:
        return True
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
primes = set()
for i in range(2, 1_000_000):
    if is_prime(i):
        primes.add(i)
circular = set()

def is_circular_prime(primes: set[int], p: int) -> bool:
    return all(int(str(p)[i:] + str(p)[:i]) in primes for i in range(len(str(p))))
for p in primes:
    if is_circular_prime(primes, p):
        circular.add(p)
print(len(circular))



