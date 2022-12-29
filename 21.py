from math import *
from collections import defaultdict
def divisors(n: int) -> set[int]:
    divisors = set()
    for i in range(1, ceil(sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return divisors - {n}
amicables = dict()
for i in range(10_000):
    amicables[i] = sum(divisors(i))
res = 0
for i in amicables:
    if amicables[i] in amicables and amicables[i] != i and  amicables[amicables[i]] == i:
        res += i
print(res)