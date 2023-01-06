""""
triangle must be isoceles, which means base is unique side
and height is derived from half base and repeated side
"""
from collections import Counter
from math import sqrt
def area(sides: tuple[int, int, int]):
    counts = Counter(sides).most_common()
    base = counts[1][0]
    repeated_side = counts[0][0]
    height = sqrt(repeated_side**2-base**2/4)
    return base * height / 2

assert area((5,5,6)) == 12
# base must be even since base**2/4 must be integral
# if smallest side exceeds target // 3, we're done
# down to 600, 000, 000 checks
# since sqrt(repeated_side**2-base**2/4) /2 must be integral
# we must have repeated_side**2-base**2/4 is even since even*even = even
# which implies base**2/4 is odd
from math import floor
target = 1_000_000_000
dist = 4
triangles = set()
while int(sqrt(dist**2/4)) - 1 < target // 3:
    side = int(sqrt(dist**2/4))
    for triangle in [(side-1, side, side), (side+1, side, side)]:
        a = area(triangle)
        if floor(a) == a and sum(triangle) <= target:
            triangles.add(triangle)
            # print(triangle)
            if len(triangles) % 100 == 0:
                print('100 found')
    dist += 2
print(sum(sum(t) for t in triangles))
