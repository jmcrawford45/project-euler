def midpoint(l: list[list[int]]) -> tuple[float, float]:
    return (sum(p[0] for p in l) / len(l), sum(p[1] for p in l) / len(l))

def equation(p1, p2):
    first = min(p1, p2)
    second = max(p1, p2)
    if second[0] - first[0] == 0:
        return lambda p: first[0] > p[1]
    slope = (second[1] - first[1]) / (second[0] - first[0])
    intercept = p1[1] - slope * p1[0]
    return lambda p: (slope * p[0] + intercept) > p[1]
res = 0
with open('triangles.txt') as f:
    for line in f.read().strip().splitlines():
        v = [int(p) for p in line.strip().split(",")]
        a,b,c = v[:2], v[2:4], v[4:]
        center = midpoint([a,b,c])
        equations = equation(a,b), equation(b,c), equation(a,c)
        below_eqs = tuple(e(center) for e in equations)
        if tuple(e((0,0)) for e in equations) == below_eqs:
            res += 1
print(res)
