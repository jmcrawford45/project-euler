from itertools import product
def num_int_coords_in_circle(r) -> int:
    # (2 * r - 1) ** 2
    axis = 4 * (r-1)
    origin = 1
    other = 4 * len([a**2 + b**2 < r ** 2 for a, b in product(range(1,r), range(1,r))])
    return axis + origin + other

print(num_int_coords_in_circle(3))
assert num_int_coords_in_circle(1) == 1
assert num_int_coords_in_circle(2) == 9