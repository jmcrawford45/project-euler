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

def is_palindrome(n: int) -> bool:
    return int(''.join(reversed(str(n)))) == n

reversible_prime_squares: set[int] = set()
curr = 3
prime_squares = set()
while len(reversible_prime_squares) < 50:
    while str(curr**2)[:-1] not in set('159') and str(curr**2)[:1] not in set('159') and not is_prime(curr):
        curr += 2
    prime_squares.add(curr ** 2)
    candidate = int(''.join(reversed(str(curr**2))))
    if (not is_palindrome(curr ** 2)) and candidate in prime_squares:
        print(curr**2, candidate)
        reversible_prime_squares.add(curr ** 2)
        if candidate < curr ** 2:
            reversible_prime_squares.add(candidate)
    curr += 2
    

print(sum(sorted(reversible_prime_squares)))