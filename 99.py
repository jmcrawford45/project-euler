from math import log2
with open('base_exp.txt') as f:
    pairs = [[int(c) for c in line.strip().split(',')] for line in f.read().strip().splitlines()]
max_idx = 0
max_seen = float('-inf')
for line, pair in enumerate(pairs):
    base, exp = pair
    base2_exp = log2(base) * exp
    if base2_exp > max_seen:
        max_seen = base2_exp
        max_idx = line
    
print(max_idx+1)