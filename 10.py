candidates = set(range(2, 2_000_000))
for i in range(2, 2_000_000):
    for j in range(i+i, 2_000_000, i):
        if j in candidates:
            candidates.remove(j)
print(sum(candidates))