from functools import lru_cache

@lru_cache(maxsize=None)
def _count_steps(digits: int, prev: int, used) -> int:
    if digits == 0:
        return int(all(used))
    res = 0
    if prev < 9:
        new_used = list(used)
        new_used[prev+1] = True
        res += _count_steps(digits - 1, prev + 1, tuple(new_used))
    if prev > 0:
        new_used = list(used)
        new_used[prev-1] = True
        res += _count_steps(digits - 1, prev - 1, tuple(new_used))
    return res

def count_steps(digits: int, usable: range) -> int:
    used = (False,) * (10)
    res = 0
    for in_len in range(len(used), digits+1):
        res += sum(_count_steps(in_len-1, i, used[:i] + (True,) + used[i+1:]) for i in usable)
    return res
print(count_steps(40, range(1, 10)))