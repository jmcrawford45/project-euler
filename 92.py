from functools import lru_cache

@lru_cache(maxsize=None)
def cycle_89(n: int) -> bool:
    if n == 1:
        return False
    if n == 89:
        return True
    return cycle_89(sum(int(c)**2 for c in str(n)))

assert cycle_89(85)
assert not cycle_89(44)
print(len([i for i in range(1, 10_000_000) if cycle_89(i)]))
