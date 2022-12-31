def reversible(n) -> bool:
    s = str(n)
    if int(s[:1]) % 2 == int(s[-1:]) % 2:
        return False
    if s.endswith('0'):
        return False
    rev_sum = int(''.join(reversed(s))) + n
    return not (set(str(rev_sum)) - set("13579"))

def rev_below(n) -> int:
    return len([i for i in range(1, n) if reversible(i)])
assert rev_below(1000) == 120
print(rev_below(1_000_000_000))
