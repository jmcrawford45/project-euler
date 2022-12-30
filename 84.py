from random import randint, choice
from collections import defaultdict
squares = list(range(40))
curr = 0
counts = defaultdict(int)
prev_rolls = []
sides = 4
def next_r(curr: int) -> int:
    while True:
        if curr in [5,15,25,35]:
            return curr
        curr += 1
        curr %= len(squares)

def next_u(curr: int) -> int:
    while True:
        if curr in [12, 28]:
            return curr
        curr += 1
        curr %= len(squares)

for _ in range(1_000_000):
    roll = (randint(1,sides), randint(1,sides))
    curr += sum(roll)
    curr %= len(squares)
    if len(prev_rolls) == 3:
        del prev_rolls[0]
    prev_rolls.append(roll)
    if min(roll) == max(roll) and len(set(prev_rolls)) == 1 and len(prev_rolls) == 3:
        curr = 10
        prev_rolls = []
    if curr == 30:
        curr = 10
    if curr in [7, 22, 36]:  # chance
        curr = choice([curr] * 6 + [0, 10, 11, 24, 39, 5, next_r(curr), next_r(curr), next_u(curr), (curr-3) % len(squares)])
    if curr in [2, 17, 33]:  # cc
        curr = choice([curr] * 14 + [0, 10])
    counts[curr] += 1
print(sorted([tuple(reversed(pair)) for pair in counts.items()], reverse=True)[:3])
