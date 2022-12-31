from math import *
from functools import lru_cache
@lru_cache
def num_divisors(n: int) -> int:
    divisors = set()
    for i in range(1, ceil(sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n / i)
    return len(divisors)
res = 0
for n in range(1, 10**7+1):
    if n % 10**5 == 0:
        print(n/10**7)
    if num_divisors(n) == num_divisors(n+1):
        res += 1
print(res)
