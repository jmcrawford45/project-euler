from math import *
def is_prime(n: int) -> bool:
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
# since always prime between n and 2n, max in 20 term sum must be at most half of sum
primes = [p for p in range(2, 1_000_000) if is_prime(p)]
window = 21
index = 0
res = 953
while sum(primes[index:index+window]) < 1_000_000:
    while sum(primes[index:index+window]) < 1_000_000:
        if is_prime(sum(primes[index:index+window])):
            res = sum(primes[index:index+window])
        index += 1
    index = 0
    window += 1
assert is_prime(res)
print(res)