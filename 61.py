def triangle(n): 
    return n*(n+1)//2
def square(n):
    return n**2
def pentagon(n):
    return n*(3*n-1)//2
def hexagon(n): return n*(2*n-1)
def heptagon(n): return n*(5*n-3)//2
def octagon(n): return n*(3*n-2)
from collections import defaultdict
functions = (triangle, square, pentagon, hexagon, heptagon, octagon)
maps = {f.__name__: defaultdict(set) for f in functions}
numbers = defaultdict(set)
for f in functions:
    curr = 1
    next = f(curr)
    while next < 10_000:
        if next >= 1_000:
            maps[f.__name__][str(next)[:2]].add(next)
            numbers[f.__name__].add(next)
        curr += 1
        next = f(curr)
octagons = set([])
for nums in maps[octagon.__name__].values():
    octagons |= nums
def find_cycle(maps: dict[str, defaultdict[str, set[int]]], cycle: list[int], seen: set[str], curr: int):
    if len(cycle) == len(maps) and str(cycle[0])[:2] == str(cycle[-1])[-2:]:
        print(sum(cycle))
    else:
        for f in set(maps) - seen:
            idx = str(curr)[-2:]
            for num in maps[f][idx]:
                if num not in cycle:
                    find_cycle(maps, cycle + [num], seen | set([f]), num)
for start in octagons:
    find_cycle(maps, [start], set([octagon.__name__]), start)
assert 8128 in maps[triangle.__name__]["81"]
assert 8281 in maps[square.__name__]["82"]
assert 2882 in maps[pentagon.__name__]["28"]