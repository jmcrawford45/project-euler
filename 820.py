def invert(k: int, n: int):
    if k == 1:
        return 0
    remainder = 10
    out = []
    remainders = []
    seen = set()
    while remainder != 0:
        if len(out) == n:
            return out[-1]
        if remainder in seen:
            break
        seen.add(remainder)
        remainders.append(remainder)
        out.append(remainder // k)
        remainder = (remainder % k) * 10
    if remainder == 0:
        return remainder
    cycle_len = len(remainders) - remainders.index(remainder)
    return out[remainders.index(remainder) + (n-1-len(remainders)) % cycle_len]

def S(n: int) -> int:
    res = 0
    for k in range(1,n+1):
        if k % 10**4 == 0:
            print("1%")
        res += invert(k, n)
    return res

assert invert(1, 7) == 0
assert invert(2, 7) == 0
assert invert(4, 7) == 0
assert invert(5, 7) == 0
assert invert(3, 7) == 3
assert invert(6, 7) == 6
assert invert(7, 7) == 1
assert S(7) == 10
assert S(100) == 418
print(S(10**7))
