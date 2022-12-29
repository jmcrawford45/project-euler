res = 0
for i in range(10000):  # n > 1 implies len(str(n*1)) < 5
    curr = 1
    out = ""
    while len(out) < 9:
        out += str(i * curr)
        curr += 1
    if len(out) == len(set(out)) and '0' not in out:
        res = max(res, int(out))
print(res)
