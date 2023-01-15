# 16 digit string implies 10 is external
from itertools import permutations
res = 0
for digits in permutations(range(1, 11)):
    lines = [
        (digits[0], digits[1], digits[2]),
        (digits[3], digits[2], digits[4]),
        (digits[5], digits[4], digits[6]),
        (digits[7], digits[6], digits[8]),
        (digits[9], digits[8], digits[1]),
    ]
    line_sum = sum(lines[0])
    # magic
    if any(sum(l) != line_sum for l in lines):
        continue
    # 16 digit
    if all(l[0] != 10 for l in lines):
        continue
    _, start_index = min((l[0], i) for i, l in enumerate(lines))
    lines = lines[start_index:] + lines[:start_index]
    num = int(''.join(''.join(str(c) for c in l) for l in lines))
    res = max(res, num)
print(res)