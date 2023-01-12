from functools import lru_cache

@lru_cache(maxsize=None)
def _count_steps(digits: int, prev: int, used) -> int:
    if digits == 0 and all(used):
        return 1
    if digits == 0:
        return 0
    res = 0
    if prev < len(used):
        res += _count_steps(digits - 1, prev + 1, used[:prev] + (True,) + used[prev+1:])
    if prev > 0:
        res += _count_steps(digits - 1, prev - 1, used[:prev-1] + (True,) + used[prev:])
    return res

def count_steps(digits: int, usable: range) -> int:
    used = (False,) * (len(usable)+1)
    res = 0
    for in_len in range(len(usable), digits+1):
        res += sum(_count_steps(in_len, i, used[:i] + (True,) + used[i+1:]) for i in usable)
    return res
print(count_steps(40, range(1, 10)))