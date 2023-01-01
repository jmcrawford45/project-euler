from math import floor
def max_with_tiles(tiles) -> int:
    res = 0
    print(floor(tiles/4 - 1))
    for i in range(floor(tiles/4 - 1)+1):
        remainder = tiles - (i+1)*4
        curr = i - 2
        while True:
            # print(i, curr, remainder)
            if curr >= -1 and remainder >= 0:
                res += 1
            else:
                break
            remainder -= (curr+1)*4
            curr -= 2
    return res


assert max_with_tiles(9) == 1
assert max_with_tiles(12) == 2
assert max_with_tiles(32) == 9
print(max_with_tiles(1_000_000))
# 1,4,8,12,16,20,24,28,32
# 1,2,3,4, 5,  6, 7, 8, 9