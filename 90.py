# single digits
# cube1.extend([0,8, 6 or 9])
# cube2.extend([1, 4, 6 or 9])
from itertools import product, combinations
seen = set()

def in_cube(num, cube) -> bool:
    return num in cube or (num == 6 and 9 in cube) or (num == 9 and 6 in cube)

def valid(cube1, cube2):
    if len(set(cube1)) != len(cube1) or len(set(cube2)) != len(cube2):
        # duplicates
        return False
    for i in range(1, 10):
        c2c1 = in_cube(i**2 % 10, cube1) and in_cube(i**2 // 10, cube2)
        c1c2 = in_cube(i**2 % 10, cube2) and in_cube(i**2 // 10, cube1)
        if not (c2c1 or c1c2):
            return False
        
    return True

assert valid((0,5,6,7,8,9), (1,2,3,4,8,9))
assert valid((0,5,6,7,8,9), (1,2,3,4,6,7))
    
cube1_sides = set(range(10))
cube2_sides = set(range(10))
for cube1 in combinations(cube1_sides, 6):
    for cube2 in combinations(cube2_sides, 6):
        if valid(cube1, cube2):
            c1 = tuple(sorted(cube1))
            c2 = tuple(sorted(cube2))
            seen.add(min(c1, c2) + max(c1, c2))
for combo in list(sorted(seen)):
    print(combo)
print(len(seen))

