from math import floor,sqrt
from collections import defaultdict
def F(n) -> int:
    res = 0
    b = 2
    seen = defaultdict(set)
    sixths = set()
    curr = 2
    while curr ** 6 <= n:
        sixths.add(curr**6)
        curr += 1

    while b ** 3 * 4 <= n:
        multiplier = b**3
        low = 2
        high = floor(pow(n/multiplier, 1/2))
        while low < high:
            mid = (low + high) // 2
            if mid ** 2 * multiplier > n:
                high = mid - 1
            elif mid ** 2 * multiplier < n:
                low = mid + 1
            else:
                low = high = mid + 1
        interval = (high - 1)
        for a in range(2, interval+2):
            seen[a**2*b**3].add((a,b))
        if low ** 2 * multiplier < n:
            interval = (low - 1)
        res += interval
        # if b**3 in sixths:
        #     print('here')
        #     res -= floor(pow((interval+1)**2, 1/6))
        for a in range(2,interval+2):
            seen[a**2*b**3].add(f"{a,b=} {a**2*b**3=}")
        b += 1
    for k,v in sorted(seen.items()):
        if len(v) > 1:
            for v1 in v:
                print(v1)
    return res
"""
16, 2 = 2048
2, 8 = 2048
3, 8 = 4608
24, 2= 4608
2, 12 = 6912
16, 3 = 6912
4, 8 = 8192
32, 2 = 8192
"""

# print(F(2*10**4))
print(F(10**4))
# 48(F(9*10**18))
# assert F(100) == 2
# print(F(2*10**4))
# assert F(2*10**4) == 130
# assert F(3*10**6) == 2014
# print(F(9*10**18))