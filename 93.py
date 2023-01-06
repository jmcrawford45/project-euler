from itertools import combinations_with_replacement, permutations, product
from math import floor
from operator import *

def try_add(curr, res: set[int]):
    try:
        floor(curr)
    except (ValueError, OverflowError):
        return
    if floor(curr) == curr and floor(curr) >= 1:
        res.add(floor(curr))


def reachable(digits) -> set[int]:
    res = set()
    for op1, op2, op3 in product([add, sub, mul, truediv], repeat=3):
        try:
            curr = op1(op2(op3(digits[0], digits[1]), digits[2]), digits[3])
            try_add(curr, res)
        except ArithmeticError:
            pass
        try:
            curr = op1(op2(digits[0], op3(digits[1], digits[2])), digits[3])
            try_add(curr, res)
        except ArithmeticError:
            pass
        try:
            curr = op1(op2(digits[0], digits[1]), op3(digits[2], digits[3]))
            try_add(curr, res)
        except ArithmeticError:
            pass
        try:
            curr = op1(digits[0], op2(digits[1], op3(digits[2], digits[3])))
            try_add(curr, res)
        except ArithmeticError:
            pass
    return res
digits = list(range(10))
max_consecutive = 0
res = []
for trial in combinations_with_replacement(digits, 4):
    seen = set()
    for order in permutations(trial):
        seen |= reachable(order)
    print(len(seen))
    curr = 1
    while curr in seen:
        curr += 1
    if curr > max_consecutive:
        max_consecutive = curr
        res = trial
    
    
print(res)