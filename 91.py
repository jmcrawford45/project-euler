from itertools import product
seen = set()
for x1, x2, y1, y2 in product(range(51), repeat=4):
    sides_squared = (x1**2+y1**2, x2**2+y2**2, (x2-x1)**2+(y2-y1)**2)
    if not all(sides_squared):
        continue
    c_squared = max(sides_squared)
    if 2*c_squared == sum(sides_squared):
        seen.add(tuple(sorted([(x1, y1), (x2, y2)])))
print(len(seen))
