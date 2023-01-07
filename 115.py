from functools import lru_cache

@lru_cache(maxsize=None)
def count_combos(block_size: int, min_len: int) -> int:
    if block_size < min_len:
        return 1
    # skip tile
    res = count_combos(block_size-1, min_len)
    # add tile
    for i in range(min_len, block_size + 1):
        res += count_combos(block_size - (i+1), min_len)
    return res

n = 0
while count_combos(n, 50) < 1_000_000:
    n += 1
print(n)