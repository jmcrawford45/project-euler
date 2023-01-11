from math import *
def triple(n, m):
    # use euler's equation to generate
    assert m > n > 0
    return tuple(sorted((2*n*m, m**2-n**2, n**2+m**2)))
target = 100_000_000
from collections import defaultdict
triangles = defaultdict(set)
res = 0
for m in range(1, floor(sqrt(target))+1):
    for n in range(1, m):
        triangle = triple(n, m)
        if sum(triangle) > target:
            break
        curr = 1
        original = triangle
        while sum(triangle) < target:
            triangle = tuple(t*curr for t in original)
            if max(triangle) % abs(triangle[0]-triangle[1]) == 0:
                res += 1
            curr += 1
print(res)
