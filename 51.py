from utils import *

def distance(x, y):
    res = []
    for i, pair in enumerate(zip(str(x),str(y))):
        c1, c2 = pair
        if c1 != c2:
            res.append(i)
    if len(set(str(x)[i] for i in res)) == 1 and len(set(str(y)[i] for i in res)) == 1:
        return tuple(res)
    return None

assert distance(13, 23) == (0,)
assert distance(13, 23) == distance(53, 73)
from collections import defaultdict
primes_distances = defaultdict(set)

digits = 1
found = set()
while not found:
    primes = primes_in_range(max(2, 10**(digits-1)), 10**digits)
    print(digits, len(primes))
    for i, p1 in enumerate(primes):
        for p2 in primes[i+1:]:
            d = distance(p1, p2)
            if d is not None:
                primes_distances[p1, d].add(p2)
        for k, v in primes_distances.items():
            if len(v) == 8-1 and k[0] not in found:
                print([k[0]] + list(v))
                found |= set([k[0]]) | v
    digits += 1
print(found)
print(min(found))


