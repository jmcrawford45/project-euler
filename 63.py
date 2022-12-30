res = set()
for i in range(1, 50):
    curr = 1
    while curr ** i < 10 ** (i+1):
        if len(str(curr**i)) == i:
            res.add((curr, i))
        curr += 1


print(len(res))