from functools import lru_cache

@lru_cache
def count_sums(n: int, high: int) -> int:
    if n == 0:
        return 1
    return sum(count_sums(n-i, i) for i in range(1, min(n+1, high+1)))
print(count_sums(100,99))