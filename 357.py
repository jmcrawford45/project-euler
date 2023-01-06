"""
prime generators must be 
    even because odd = odd * odd and odd+odd=even which isn't prime
    not divisible by 4 since if d is even, n/d must be odd
"""
from utils import *

def prime_generator(n) -> bool:
    d = list(sorted(divisors(n)))
    for a, b in zip(d[:len(d)//2], reversed(d[len(d)//2:])):
        if not is_prime(a+b):
            return False
    return True

curr = 2
res = 0
while curr <= 100_000_000:
    if curr % 1_000_000 == 2:
        print('here')
    if prime_generator(curr):
        res += curr
    curr += 4