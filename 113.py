from functools import lru_cache

@lru_cache(maxsize=None)
def count_increasing(num_digits: int, min_digit: int, max_digit: int) -> int:
    if num_digits == 0:
        return 1
    return sum(count_increasing(num_digits-1, i, max_digit) for i in range(min_digit, max_digit+1))

@lru_cache(maxsize=None)
def count_decreasing(num_digits: int, min_digit: int, max_digit: int) -> int:
    if num_digits == 0:
        return 1
    res = sum(count_decreasing(num_digits-1, min_digit, i) for i in range(min_digit+1, max_digit+1))
    return res + count_decreasing(num_digits-1, min_digit, max_digit)

def is_increasing(n: int) -> bool:
    return ''.join(sorted(str(n))) == str(n)

def is_decreasing(n: int) -> bool:
    return ''.join(sorted(str(n), reverse=True)) == str(n)
# for i in range(1000):
#     if is_decreasing(i) and is_increasing(i):
#         print(i)
# print(count_decreasing(3, 0, 9))
print(len([i for i in range(100) if is_decreasing(i)]))
print(count_decreasing(2, 0, 9))
assert (len([i for i in range(100) if is_decreasing(i)])) == count_decreasing(2, 0, 9)

assert len([i for i in range(100) if is_increasing(i)]) == 55

def count_non_bouncy(num_digits) -> int:
    # for every len >=2, we can have e.g. 111, 222, 333 as both increasing and decreasing
    # for len 1, we have 0 as both
    double_counts = (9*(num_digits-1)) + 10
    return count_increasing(num_digits, 0, 9) + count_decreasing(num_digits,0,9) - double_counts
print((len([i for i in range(100) if (is_decreasing(i) or is_increasing(i))])))
print(count_non_bouncy(2))
assert (len([i for i in range(100) if (is_decreasing(i) or is_increasing(i))])) == count_non_bouncy(2)
print((len([i for i in range(1_000_000) if (is_decreasing(i) or is_increasing(i))])) )
assert (len([i for i in range(1_000_000) if (is_decreasing(i) or is_increasing(i))])) == count_non_bouncy(6)


assert count_increasing(1, 0, 9) == 10
print(count_non_bouncy(2))
assert count_non_bouncy(2) == 100
print(count_non_bouncy(10))
assert 2*count_increasing(2, 0, 9) == 100
print(2*count_increasing(6, 0, 9))
# assert 1_000_000 - 2*count_increasing(6, 0, 9) == 12951