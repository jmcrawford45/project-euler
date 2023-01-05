from math import sqrt, floor
def get_period(n):
    if floor(sqrt(n)) == sqrt(n):
        return []
    cycle = []
    seen = set()
    a = floor(sqrt(n))
    prev = None
    denom = sqrt(n)-a
    while (a, prev) not in seen:
        seen.add((a, prev))
        prev = a
        cycle.append(a)
        a = floor(1/(denom))
        denom = (1/denom-a)
    print(n, cycle)
    cycle = cycle[1:]
    if cycle[0] == cycle[-1] and len(cycle) >= 2:
        cycle = cycle[:-1]
    return cycle
print(get_period(23))
assert get_period(23) == [1,3,1,8]

def odd_periods_below(n) -> int:
    count = 0
    for i in range(2, n+1):
        print(i, get_period(n))
        # if len(get_period(n)) % 2 == 1:
        #     count += 1
    return count
print(odd_periods_below(13))
# assert odd_periods_below(13) == 4