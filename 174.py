from math import floor
from collections import defaultdict
# def max_with_tiles(tiles) -> int:
#     res = 0
#     for i in range(floor(tiles/4 - 1)+1):
#         if res > 15:
#             return 0
#         remainder = tiles - (i+1)*4
#         curr = i - 2
#         while True:
#             # print(i, curr, remainder)
#             if curr >= -1 and remainder == 0:
#                 res += 1
#             elif remainder < 0 or curr < -1:
#                 break
#             remainder -= (curr+1)*4
#             curr -= 2
#     return res
# res = defaultdict(int)
# for i in range(1, 1_000_001):
#     if i % 10**4 == 0:
#         print(f"{i//10**4}%")
#     res[max_with_tiles(i)] += 1
# for k, v in res.items():
#     print(f"{k}: {v}")
# print(res[15])
# assert res[15] == 832
# print(sum(res[i] for i in range(1,11)))
from collections import *
odds = 1
squares = []
res = defaultdict(int)
top = 10**6
while 2*odds + 1 <= top:
    if (odds - 1) % 10**4 == 0:
        print(f"{(odds - 1)/(10**4)}%")
    next_square = odds ** 2
    for s in squares:
        res[next_square-s] += 1
    squares.append(next_square)
    odds += 2
evens = 2
squares = []
while 2*evens + 1 <= top:
    next_square = evens ** 2
    for s in squares:
        res[next_square-s] += 1
    squares.append(next_square)
    evens += 2
counts = Counter(res.values())
print(counts[15])