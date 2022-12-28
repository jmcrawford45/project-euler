from math import *
def supports_conjecture(n: int, primes: set[int], twice_squares: set[int]) -> bool:
    if n % 2 == 0 or n in primes:
        return True
    while max(twice_squares) < n:
        twice_squares.add(2* (1+len(twice_squares))**2)
    for twice_square in twice_squares:
        if n - twice_square in primes:
            return True
    return False

def is_prime(n: int) -> bool:
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = set()
twice_squares = set([2])

curr = 3
while True:
    if is_prime(curr):
        primes.add(curr)
    elif not supports_conjecture(curr, primes, twice_squares):
        print(curr)
        break
    curr += 2


