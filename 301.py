"""
idea: since a loss occurs with the bitwise xor of heap sizes is 0
to start, and since 2n = n << 1, and since n xor 2n xor 3n = 0
only when n xor 2n = 3n, we must have no consecutive ones in the
bitwise representation of n. Thus, we can count all bit strings
of length 30 or less which have no consecutive ones.
"""
from functools import lru_cache

@lru_cache(maxsize=None)
def non_consec_one_bit_str(prev: int, size: int) -> int:
    if size == 0:
        return 1
    res = non_consec_one_bit_str(0, size - 1)
    if prev != 1:
        res += non_consec_one_bit_str(1, size - 1)
    return res

print(non_consec_one_bit_str(0, 30))