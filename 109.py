scores = (
    [("S" + str(i), i) for i in range(1,21)] +
    [("D" + str(i), i*2) for i in range(1,21)] +
    [("T" + str(i), i*3) for i in range(1,21)] +
    [("SB25", 25), ("DB50", 50)]
)
doubles = [i*2 for i in range(1,21)] + [50]

from itertools import product
def num_checkouts(target: int) -> int:
    checkouts = set()
    for t1, t2, t3 in product(scores, repeat=3):
        throw1, score1 = t1
        throw2, score2 = t2
        throw3, score3 = t3
        if sum([score1, score2, score3]) == target and throw3.startswith('D'):
            checkouts.add((min(throw1, throw2), max(throw1, throw2), throw3))
    for t1, t2 in product(scores, repeat=2):
        throw1, score1 = t1
        throw2, score2 = t2
        if sum([score1, score2]) == target and throw2.startswith('D'):
            checkouts.add((throw1, throw2))
    for t1 in scores:
        throw1, score1 = t1
        if score1 == target and throw1.startswith('D'):
            checkouts.add((throw1,))
    return len(checkouts)
assert num_checkouts(6) == 11
print(sum(num_checkouts(i) for i in range(2, 100)))

