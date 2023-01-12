rings = [
    [range(2,8)],
    [range(8,20)],
    [range(20,39)],
]

pd = set()
while len(pd) != 2000:
    for i, num in enumerate(rings[1]):
        next_ring_neighbors = i*2
        curr_ring = [rings[i-1 % len(rings[1])], rings[i+1 % len(rings[1])]]
        prev_ring = []
