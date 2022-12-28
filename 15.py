from functools import lru_cache

@lru_cache(maxsize=None)
def lattice_routes(right_remaining: int, steps_remaining: int) -> int:
    if right_remaining == 0 or steps_remaining == 0:
        return 1
    res = lattice_routes(right_remaining - 1, steps_remaining - 1)
    if right_remaining < steps_remaining:
        res += lattice_routes(right_remaining, steps_remaining - 1)
    return res

assert lattice_routes(1, 2) == 2
assert lattice_routes(2, 4) == 6
print(lattice_routes(20, 40))