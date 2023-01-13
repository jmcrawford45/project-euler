from functools import lru_cache

@lru_cache(maxsize=None)
def prize_strings(days: int, consecutive_abs: int, num_late: int) -> int:
    if consecutive_abs == 3 or num_late > 1:
        return 0
    if days == 0:
        return 1
    return prize_strings(days - 1, 0, num_late) + prize_strings(days - 1, 0, num_late + 1) + prize_strings(days - 1, consecutive_abs + 1, num_late)
assert prize_strings(4, 0,  0) == 43
print(prize_strings(30, 0, 0))