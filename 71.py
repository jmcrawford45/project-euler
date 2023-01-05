min_dist = float('inf')
best = None
from math import floor
for d in range(1, 1_000_000):
    dist = abs(floor(d * 3/7) / d - 3/7)
    if dist < min_dist and dist != 0:
        min_dist = dist
        best = floor(d * 3/7)
print(best)
