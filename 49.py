from math import *
from collections import Counter
def is_prime(n: int) -> bool:
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_permutations(n: int) -> bool:
    if all(is_prime(i*3330 + n) and Counter(str(i*3330 + n)) == Counter(str(n)) for i in range(3)):
        return True

seen = set()
for n in range(1000, 10_000):
    if prime_permutations(n) and n not in {1487, 4817, 8147}:
        print(''.join(str(i*3330 + n) for i in range(3)))