from functools import lru_cache
from math import log10, floor
import sys
sys.setrecursionlimit(10**6)
modulus = 1_000_000_007

@lru_cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

@lru_cache(maxsize=None)
def s(n, optimize=True):
    num_nines, remainder = divmod(n, 9)
    if n > 81 and optimize:  # 9*(log10(p)-1)
        non_cycle_offset = -1 + -7 * (remainder+1) * pow(10, num_nines-9, modulus)
        return (non_cycle_offset) % modulus
    return int(str(remainder) + ('9' * num_nines)) % modulus

@lru_cache
def S(n):
    if n == 0:
        return 0
    return s(n) + S(n-1)
assert s(10) == 19
assert S(20) == 1074
assert s(81) == (-8 % modulus)
assert s(82) == (-15 % modulus)
assert s(83) == (-22 % modulus)
assert s(84) == (-29 % modulus)
assert s(85) == (-36 % modulus)
assert s(86) == (-43 % modulus)
assert s(87) == (-50 % modulus)
assert s(88) == (-57 % modulus)
assert s(89) == (-64 % modulus)
assert s(90) == (-71 % modulus)
assert s(91) == s(91, False)
res = 0
for i in range(2, 91):
    print(i)
    res = (res + S(fibonacci(i))) % modulus
print(res)