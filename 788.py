from functools import lru_cache
modulus = 1_000_000_007
import sys
sys.setrecursionlimit(10**6)

@lru_cache(maxsize=None)
def factorial(n):
    if n <= 1:
        return 1
    return (n*factorial(n-1)) % modulus

def inv(n):
    return pow(n, -1, modulus)

def comb(n, r):
    return (factorial(n) * inv(factorial(r) * factorial(n-r))) % modulus

@lru_cache(maxsize=None)
def majority_count(majority, num_digits, top = None) -> int:
    if top is None:
        top = num_digits+1
    if majority > num_digits:
        return 0
    count = 0
    for i in range(majority, top):
        # all digits except majority digit
        minority_combos = (9 ** (num_digits-i))
        count += comb(num_digits, i) * minority_combos
        count %= modulus
    return count

@lru_cache(maxsize=None)
def d(n):
    print(n)
    if n == 0:
        return 0
    num_digits = len(str(10**n-1))
    majority = num_digits // 2 + 1
    non_zero_digit_dominators = 10*(majority_count(majority, num_digits))
    to_remove = 1 + majority_count(majority, num_digits, num_digits)
    return (d(n-1) + non_zero_digit_dominators - to_remove) % modulus
assert d(3) == 270
assert d(4) == 603
assert d(5) == 8307
assert d(10) == 21893256
print(d(2022))
