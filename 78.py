from functools import lru_cache

@lru_cache(maxsize=None)
def count_sums(n: int, high: int) -> int:
    if n == 0:
        return 1
    return sum(count_sums(n-i, i) for i in range(1, min(n+1, high+1)))
assert count_sums(5,5) == 7
curr = 0
while count_sums(curr, curr) % 1_000_000 != 0:
    curr += 1
print(curr)