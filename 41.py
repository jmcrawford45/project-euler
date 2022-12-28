from itertools import permutations
from math import ceil, sqrt
n = 9
max_seen = 0

def is_prime(n: int) -> bool:
    for i in range(2, ceil(sqrt(n))):
        if n % i == 0:
            return False
    return True


while True:
    for order in permutations(range(1, n+1)):
        num = int(''.join(str(i) for i in order))
        if is_prime(num):
            max_seen = max(max_seen, num)
    if max_seen:
        break
    n -= 1
print(max_seen)
