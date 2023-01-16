from math import *
def triple(n, m):
    # use euler's equation to generate
    assert m > n > 0
    return tuple(sorted((2*n*m, m**2-n**2, n**2+m**2)))

def add_triangle(pair_counts, triangle) -> bool:
    pair_counts[triangle[:2]] += 1
    pair_counts[triangle[1:]] += 1
    pair_counts[triangle[:1] + triangle[2:]] += 1
    return all([
        pair_counts[triangle[:2]] == 2,
        pair_counts[triangle[1:]] == 2,
        pair_counts[triangle[:1] + triangle[2:]] == 2,
    ])

target = 100_500_000
from collections import defaultdict
import sys
pair_counts = defaultdict(int)
seen = set()
for m in range(1, floor(sqrt(target))+1):
    for n in range(1, m):
        triangle = triple(n, m)
        if sum(triangle) > target:
            break
        
        k = 1
        while k*sum(triangle) < target:
            next_triangle = tuple(s*k for s in triangle)
            if next_triangle not in seen and add_triangle(pair_counts, next_triangle):
                print(next_triangle)
                sys.exit()
            seen.add(next_triangle)
            k += 1

