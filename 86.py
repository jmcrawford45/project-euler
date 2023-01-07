from math import *
def triple(n, m):
    # use euler's equation to generate
    assert m > n > 0
    return tuple(sorted((2*n*m, m**2-n**2, n**2+m**2)))
target = 1_500_000
from collections import defaultdict
triangles = defaultdict(set)
for m in range(1, floor(sqrt(target))+1):
    for n in range(1, m):
        triangle = triple(n, m)
        if sum(triangle) > target:
            break
        k = 1
        while k*sum(triangle) < target:
            triangles[k*sum(triangle)].add(tuple(s*k for s in triangle))
            k += 1
assert len(triangles[120]) == 3
print(len([v for v in triangles.values() if len(v) == 1]))
