from functools import lru_cache
alphabet_len = 26
from math import comb

def count_strings(size: int) -> int:
    # We choose size characters from the alphabet
    # Once chosen, each character set can have the increasing char pair
    # at any position from 1 to the end
    # For each increasing position i, we can pick any i-1 elements to proceed it
    # but after this we must have i is the max of the remaining chars
    # and all following chars in distinct sorted order
    return comb(26, size) * sum(comb(size, i-1) for i in range(1, size))
assert count_strings(3) == 10400
res = 0
for i in range(1, 27):
    res = max(res, count_strings(i))
print(res)

