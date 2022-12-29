from itertools import permutations
seen =  set()

def to_int(l: list[int]) -> int:
    digits = [str(c) for c in l]
    return int(''.join(digits))

for p in permutations(range(1, 10)):
    for i in range(1, len(p) - 2):
        for j in range(i+1, len(p) - 1):
            a,b,c = to_int(p[:i]), to_int(p[i:j]), to_int(p[j:])
            if a*b == c:
                seen.add(c)
print(sum(seen))