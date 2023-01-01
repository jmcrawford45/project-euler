from functools import lru_cache

@lru_cache(maxsize=None)
def at_most_digits_containing(n, contains: tuple[bool, bool, bool] = (False, False, False), non_zero: bool = False) -> int:
    if all(contains):
        return 16 ** n
    if n == 0:
        return 0
    zero, one, a = contains
    other_digits = 13 * at_most_digits_containing(n - 1, contains, True)
    add_zero = at_most_digits_containing(n-1, (non_zero, one, a), non_zero)
    add_one = at_most_digits_containing(n-1, (zero, True, a), True)
    add_a = at_most_digits_containing(n-1, (zero, one, True), True)
    return other_digits + add_a + add_one + add_zero


assert at_most_digits_containing(3) == 4
print(hex(at_most_digits_containing(16))[2:].upper())