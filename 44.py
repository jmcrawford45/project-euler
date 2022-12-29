
def pentagon(n: int) -> int:
    return n*(3*n-1)//2

pentagons = {n: pentagon(n) for n in range(1, 100)}
min_dist = float('inf')
while True:
    print(f"{len(pentagons)=}")
    values = set(pentagons.values())
    for i in range(1, len(pentagons)//2):
        for j in range(i+1, len(pentagons)//2):
            if (pentagons[i] + pentagons[j]) in values and abs(pentagons[i]-pentagons[j]) in values:
                min_dist = min(min_dist, abs(pentagons[i]-pentagons[j]))
    
    min_next_dist = abs(pentagons[len(pentagons)]-pentagons[len(pentagons)-1])
    print(f"{min_next_dist=} {min_dist=}")
    if min_next_dist > min_dist:
        break
    for i in range(len(pentagons), 2*len(pentagons)):
        pentagons[i] = pentagon(i)
print(min_dist)