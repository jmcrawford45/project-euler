"""
idea: start with a set of ones and adjust from there
"""
def product(l) -> int:
    accumulator = 1
    for e in l:
        accumulator *= e
    return accumulator

def min_prod_sum(n):
    candidate = [1] * n
    while sum(candidate) != product(candidate):
        if candidate[0] > 100:
            break
        print(candidate)
        if product(candidate) * 2 <= sum(candidate) + 1:
            candidate[candidate.index(1)] = 2
        elif product(candidate) < (sum(candidate)+1):
            candidate[candidate.index(max(candidate))] += 1
    return sum(candidate)

assert min_prod_sum(2) == 4
assert min_prod_sum(3) == 6
print(sorted(set([min_prod_sum(i) for i in range(2, 13)])))