from functools import lru_cache

@lru_cache(maxsize=None)
def _count_strings(size: int, prev) -> int:
    if size == 0:
        if sum(prev) <= 9:
            print(prev)
        return int(sum(prev) <= 9)
    res = 0
    if len(prev) < 3:
        for i in range(9-sum(prev) + 1):
            res += _count_strings(size-1, prev + (i,))
    else:
        for i in range(9-sum(prev[1:])+1):
            res += _count_strings(size-1, prev[1:] + (i,))
    return res

def count_strings(size: int) -> int:
    return sum(_count_strings(size-1, (i,)) for i in range(1, 10))

assert count_strings(1) == 9
print(count_strings(20))

