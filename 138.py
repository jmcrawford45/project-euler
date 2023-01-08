from math import *
def triple(n, m):
    # use euler's equation to generate
    assert m > n > 0
    return tuple(sorted((2*n*m, m**2-n**2, n**2+m**2)))
triangles = set()
m = 1
while len(triangles) < 12:
    for n in range(1, m):
        triangle = triple(n, m)
        if abs(2*triangle[0]-triangle[1]) == 1:
            print(triangle)
            triangles.add(triangle)
    m += 1
print(sum(max(t) for t in triangles))
