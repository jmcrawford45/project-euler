from math import comb
res = 0
for n in range(1, 101):
    for r in range(1, n):
        if comb(n, r) > 1_000_000:
            res += 1
print(res)