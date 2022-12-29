res = 0
for a in range(100):
    for b in range(100):
        res = max(res, sum(int(c) for c in str(a**b)))
print(res)