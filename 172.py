from functools import lru_cache

@lru_cache(maxsize=None)
def _count_strings(size: int, uses) -> int:
    if max(uses) == 4:
        return 0
    if size == 0:
        return 1
    res = 0
    for i in range(len(uses)):
        res += _count_strings(size-1, uses[:i] + (uses[i] + 1,) + uses[i+1:])
    return res

def count_strings(size: int) -> int:
    uses = (0,) * 10
    return sum(_count_strings(size-1, uses[:i] + (1,) + uses[i+1:]) for i in range(1, 10))

assert count_strings(1) == 9
print(count_strings(18))

