curr = 1
triangles = set()
pentagons = set()
hexagons = set()
while True:
    t = curr*(curr+1)//2
    triangles.add(t)
    pentagons.add(curr*(3*curr-1)//2)
    hexagons.add(curr*(2*curr-1))
    if t in pentagons and t in hexagons and t > 40_755:
        print(t)
        break
    curr += 1
