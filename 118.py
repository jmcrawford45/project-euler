from itertools import permutations
from functools import lru_cache
from utils import is_prime

@lru_cache(maxsize=None)
def count_splits(digits: tuple[int], max_used: int = 0) -> int:
    if not digits:
        return 1
    res = 0
    for i in range(1, len(digits)+1):
        candidate = int(''.join(str(c) for c in digits[:i]))
        if candidate > max_used and is_prime(candidate):
            res += count_splits(digits[i:], candidate)
    return res

assert count_splits((2,5,4,7,8,9,6,3,1)) == 1

res = 0
for digits in permutations(range(1, 10)):
    if digits[-1] % 2 == 0:
        continue
    res += count_splits(tuple(digits))
print(res)
