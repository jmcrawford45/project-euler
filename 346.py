from collections import defaultdict

def strong_repunits(top: int):
    repunits = defaultdict(set)
    for base in range(2, top+1):
        curr = 1
        pow = 0
        while curr < top:
            repunits[curr].add(base)
            pow += 1
            curr += base ** pow
    count = 0
    for i in range(1, top+1):
        if len(repunits[i]) >= 2:
            count += 1
    return count
assert strong_repunits(50) == 8
print(strong_repunits(10**12))

        