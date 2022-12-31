# single digits
# cube1.extend([0,8, 6 or 9])
# cube2.extend([1, 4, 6 or 9])
from itertools import product
seen = set()
def valid(cube1, cube2):
    if len(set(cube1)) != len(cube1) or len(set(cube2)) != len(cube2):
        # duplicates
        return False
    if not all(c in cube1 + cube2 for c in [2,3,5]):
        return False
    if not((2 in cube1 and 5 in cube2) or (5 in cube1 and 2 in cube2)):
        return False
    return True


    
cube1_sides = set(range(10)) - set([0,8])
cube2_sides = set(range(10)) - set([1,4])
for cube1 in product([6,9], cube1_sides, cube1_sides, cube1_sides):
    for cube2 in product([6,9], cube2_sides, cube2_sides, cube2_sides):
        if valid(cube1, cube2):
            seen.add(tuple(sorted(cube1)) + tuple(sorted(cube2)))
for combo in list(sorted(seen)):
    print(combo)
print(len(seen))

