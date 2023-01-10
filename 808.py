from math import *
from utils import *
primes = primes_in_range(2, 50_000_000)
primes_squares = set([p**2 for p in primes])

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

def is_palindrome(n: int) -> bool:
    return int(''.join(reversed(str(n)))) == n

reversible_prime_squares: set[int] = set()
prime_squares = set()
target_digits = 0
seen = set()
res = 0
for curr in primes:
    prime_squares.add(curr ** 2)
    candidate = int(''.join(reversed(str(curr**2))))
    if (not is_palindrome(curr ** 2)) and candidate in prime_squares:
        print(curr**2, candidate)
        if curr ** 2 not in seen:
            seen.add(curr**2)
            seen.add(candidate)
            res += curr**2 + candidate
        reversible_prime_squares.add(curr ** 2)
        reversible_prime_squares.add(candidate)
print(res)
    

print(sum(list(sorted(reversible_prime_squares))[:50]))