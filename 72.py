from math import ceil
from utils import gcd
def count_range(n) -> int:
    count = 0
    for denominator in range(2, n + 1):
        if denominator % 100 == 0:
            print(denominator)
        for numerator in range(ceil(denominator/3), ceil(denominator/2)+1):
            if gcd(numerator, denominator) == 1 and 1/3 < numerator / denominator < 1/2:
                count += 1
    return count
assert count_range(8) == 3
print(count_range(12_000))