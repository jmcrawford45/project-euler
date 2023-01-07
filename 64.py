from math import sqrt, floor
def get_period(n):
    if floor(sqrt(n)) == sqrt(n):
        return []
    cycle = []
    seen = set()
    a = floor(sqrt(n))
    numerator = 1
    denom_sub = a
    while (a, numerator, denom_sub) not in seen:
        """
        a0 = 4, 1/(sqrt(23)-4) = 
        """
        seen.add((a, numerator, denom_sub))
        cycle.append((a, numerator, denom_sub))
        tmp_denom = (n-denom_sub**2)//numerator
        tmp_num_add = denom_sub
        a = floor((sqrt(n)+tmp_num_add)/tmp_denom)
        numerator = tmp_denom
        denom_sub = -(tmp_num_add - a*(tmp_denom))
    cycle = cycle[cycle.index((a, numerator, denom_sub)):]
    return [c[0] for c in cycle]

assert get_period(1) == []
assert get_period(2) == [2]
assert get_period(23) == [1,3,1,8]
assert get_period(13) == [1,1,1,1,6]

def odd_periods_below(n) -> int:
    count = 0
    for i in range(2, n+1):
        if len(get_period(i)) % 2 == 1:
            count += 1
    return count
assert odd_periods_below(13) == 4
print(odd_periods_below(10_000))