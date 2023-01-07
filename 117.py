from functools import lru_cache

@lru_cache(maxsize=None)
def count_combos(block_size: int, min_len: int, max_len: int) -> int:
    if block_size < min_len:
        return 1
    # skip tile
    res = count_combos(block_size-1, min_len, max_len)
    # add tile
    for i in range(min_len, min(max_len, block_size) + 1):
        res += count_combos(block_size - i, min_len, max_len)
    return res
print(count_combos(5, 2, 4))
assert count_combos(5, 2, 4) == 15
print(count_combos(50, 2, 4))