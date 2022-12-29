from math import *
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

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
    return out if out else set(n)
curr = 14
while True:
    if all(len(prime_factors(i)) == 4 for i in range(curr, curr+4)):
        print(curr)
        break
    curr += 1