from math import *
def is_prime(n: int) -> bool:
    if n == 2:
        return True
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
count_primes = 1
curr = 3
while True:
    if is_prime(curr):
        count_primes += 1
    if count_primes == 10_001:
        print(curr)
        break
    curr += 2