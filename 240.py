from functools import lru_cache

@lru_cache(maxsize=None)
def dice_sums(num_dice: int, max: int, target: int, rolls: int, num_top: int, min_roll: int) -> int:
    if target == 0 and rolls == num_dice - num_top:
        return max ** rolls
    if target <= 0:
        return 0
    res = 0
    for i in range(1, max + 1):
        res += dice_sums(num_dice, i, target - i, rolls - 1, num_top, min(min_roll, i))

assert dice_sums(5, 6, 15, 3, 6) == 1111