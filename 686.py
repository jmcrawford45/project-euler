def p(L: str, n):
    count = 0
    power = 1
    curr = 2
    while True:
        power += 1
        curr *= 2
        if str(curr).startswith(L):
            count += 1
            if count % (n // 100+1) == 0:
                print(f"{count // (n // 100+1)}%")
        if count == n:
            return power
        if curr > 2**128:
            curr = int(str(curr)[:-8])
        

assert p("12", 1) == 7
assert p("12", 2) == 80
assert p("123", 45) == 12710
print(p("123", 678910))