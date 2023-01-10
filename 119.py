seen = set()
curr = 4
while len(seen) < 50 and curr < 10000:
    for pow in range(2, 20):
        if sum(int(c) for c in str(curr**pow)) == curr:
            seen.add(curr**pow)
            print(curr**pow)
    curr += 1
print(sorted(seen)[:30])