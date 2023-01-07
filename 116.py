from functools import lru_cache

@lru_cache(maxsize=None)
def count_combos(block_size: int, block_len: int) -> int:
    if block_size < block_len:
        return 1
    # skip tile
    res = count_combos(block_size-1, block_len)
    # add tile
    res += count_combos(block_size - block_len, block_len)
    return res

count_non_empty = lambda block_size, block_len: count_combos(block_size, block_len) - 1

assert count_non_empty(5, 2) == 7
assert count_non_empty(5, 3) == 3
assert count_non_empty(5, 4) == 2

print(sum(count_non_empty(50, i) for i in range(2,5)))