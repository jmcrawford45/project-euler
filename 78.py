from functools import lru_cache

@lru_cache(maxsize=None)
def count_sums(n: int, high: int) -> int:
    if n <= 0:
        return 1
    return sum(count_sums(n-i, min(i, n-i)) for i in range(1, min(n+1, high+1)))
assert count_sums(5,5) == 7
curr = 0
closest = float('inf')
from fractions import Fraction
for i in range(100):
    print(i, Fraction(count_sums(i, i), count_sums(i-1, i-1)))
# while count_sums(curr, curr) % 1_000_000 != 0:
#     if count_sums(curr, curr) % 1_000_000 < closest and count_sums(curr, curr) > 1_000_000:
#         closest = count_sums(curr, curr) % 1_000_000
#         print(f"closest {count_sums(curr, curr) % 1_000_000}")
#     curr += 1
# print(curr)