from utils import prime_factors
from decimal import Decimal
def M(n: int) -> int:
    """return k number of equal parts"""
    p_max = 0
    k_max = 0
    for k in reversed(range(n)):
        if p_max < Decimal(n / k) ** k:
            p_max = Decimal(n / k) ** k
            k_max = k
        else:
            break
    return k_max

def D(n: int) -> int:
    print(n)
    k = M(n)
    res = n
    for p in prime_factors(n):
        while k % p == 0 and n % p == 0:
            k //= p
            n //= p
    if k != 1 and (prime_factors(k) - set([2,5])):
        return res
    return -res


assert M(11) == 4
assert M(8) == 3

assert D(11) == -11
assert D(8) == 8
assert sum(D(n) for n in range(5, 101)) == 2438
print(sum(D(n) for n in range(5, 10_001)))