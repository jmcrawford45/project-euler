"""
Main idea: since totient is minimized when divisors are large, find largest n <= 1,000,000 that is a product of small primes
"""
from utils import is_prime
from utils import num_divisors
curr = 3
accumulator = 2
while True:
    if accumulator * curr > 1_000_000:
        break
    if is_prime(curr):
        accumulator *= curr
    curr += 2
print(accumulator)
