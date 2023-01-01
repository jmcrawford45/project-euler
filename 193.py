from utils import *

def squarefree_below(n) -> int:
    """
    Create a sieve count starting with n
    """
    primes_in_range(2, ceil(n**0.25))

assert squarefree_below(12) == 8
# print(squarefree_below(2**50))