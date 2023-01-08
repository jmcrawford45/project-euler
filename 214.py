from utils import *
from collections import defaultdict

def totient_chains(d: int, length: int) -> int:
    phi = list(range(d+1))
    primes = []
    for i, v in enumerate(phi):
        if i < 2:
            continue
        if i == v:
            primes.append(i)
            for j in range(i, len(phi), i):
                phi[j] //= i
                phi[j] *= i-1
    res = 0
    cache = dict()
    for i in primes:
        curr = i
        chain_len = 1
        while curr != 1 and chain_len <= length:
            if curr in cache:
                chain_len += cache[curr] - 1
                break
            chain_len += 1
            curr = phi[curr]
        cache[i] = chain_len
        if chain_len == length:
            res += i
    return res
assert totient_chains(18, 4) == 12
print(totient_chains(40_000_000, 25))