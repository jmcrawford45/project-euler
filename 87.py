from math import *
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
curr = 2
squares = set()
cubes = set()
fourths = set()
while curr ** 2 < 50_000_000:
    if is_prime(curr):
        if curr ** 2 < 50_000_000:
            squares.add(curr ** 2)
        else:
            break
        if curr ** 3 < 50_000_000:
            cubes.add(curr ** 3)
        if curr ** 4 < 50_000_000:
            fourths.add(curr ** 4)
    curr += 1
res = set()
for f in fourths:
    for c in cubes:
        for s in squares:
            if f+c+s < 50_000_000:
                res.add(f+c+s)
print(len(res))