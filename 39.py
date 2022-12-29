from collections import defaultdict
no_hypotenuse_square_sums = defaultdict(set)
for a in range(1, 500):
    for b in range(a, 500-a):
        no_hypotenuse_square_sums[a**2+b**2].add((a,b))
assert (3, 4) in no_hypotenuse_square_sums[25]
max_solutions = 0
res = 0
for p in range(1, 1_001):
    solutions = 0
    for c in range(p//3, p):
        sides = no_hypotenuse_square_sums[c**2]
        raw = [sides for sides in no_hypotenuse_square_sums[c**2] if p-sides[0]-sides[1] == c]
        solutions += len(raw)
    if solutions > max_solutions:
        max_solutions = solutions
        res = p
print(res)

