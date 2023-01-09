from functools import lru_cache

@lru_cache(maxsize=None)
def count_increasing(num_digits: int, min_digit: int, max_digit: int) -> int:
    if num_digits == 0:
        return 1
    return sum(count_increasing(num_digits-1, i, max_digit) for i in range(min_digit, max_digit+1))

@lru_cache(maxsize=None)
def count_decreasing(num_digits: int, min_digit: int, max_digit: int, init: bool = True) -> int:
    if num_digits == 0:
        return 1
    res = sum(count_decreasing(num_digits-1, min_digit, max_digit if init and i == 0 else i, init and i == 0) for i in range(0, max_digit+1))
    return res

def is_increasing(n: int) -> bool:
    return ''.join(sorted(str(n))) == str(n)

def is_decreasing(n: int) -> bool:
    return ''.join(sorted(str(n), reverse=True)) == str(n)
assert (len([i for i in range(100) if is_decreasing(i)])) == count_decreasing(2, 0, 9)

def count_non_bouncy(num_digits) -> int:
    # we can have e.g. 111, 222, 333 as both increasing and decreasing
    double_counts = (9*(num_digits)) + 2
    return count_increasing(num_digits, 0, 9) + count_decreasing(num_digits,0,9) - double_counts
assert 12951 == count_non_bouncy(6)
print(count_non_bouncy(100))