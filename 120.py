def max_r(a):
    print(a)
    n = 1
    res = 0
    seen = set()
    while True:
        terms = (pow(a-1, n, a**2), (pow(a+1, n, a**2)))
        r = sum(terms) % a**2
        if terms in seen:
            break
        seen.add(terms)
        res = max(res, r)
        n += 1
    return res
print(max_r(7))
assert max_r(7) == 42
print(sum(max_r(i) for i in range(3, 1001)))
