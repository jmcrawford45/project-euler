from math import *
from functools import lru_cache

@lru_cache(maxsize=None)
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

up_left = [5]
up_right = [3]
down_left = [7]
side_length = 3
while True:
    percent_prime = len([p for p in up_left + up_right + down_left if is_prime(p)]) / (1+ side_length // 2 * 4)
    print(percent_prime, side_length)
    if percent_prime < 0.1:
        break
    up_left.append(side_length ** 2 + (side_length+2) * 2 - 2)
    up_right.append(side_length ** 2 + (side_length+2) - 1)
    down_left.append(side_length ** 2 + (side_length+2)*3 - 3)
    side_length += 2
print(side_length)