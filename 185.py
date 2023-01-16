test = """
90342 ;2 correct
70794 ;0 correct
39458 ;2 correct
34109 ;1 correct
51545 ;2 correct
12531 ;1 correct
"""

problem = """
5616185650518293 ;2 correct
3847439647293047 ;1 correct
5855462940810587 ;3 correct
9742855507068353 ;3 correct
4296849643607543 ;3 correct
3174248439465858 ;1 correct
4513559094146117 ;2 correct
7890971548908067 ;3 correct
8157356344118483 ;1 correct
2615250744386899 ;2 correct
8690095851526254 ;3 correct
6375711915077050 ;1 correct
6913859173121360 ;1 correct
6442889055042768 ;2 correct
2321386104303845 ;0 correct
2326509471271448 ;2 correct
5251583379644322 ;2 correct
1748270476758276 ;3 correct
4895722652190306 ;1 correct
3041631117224635 ;3 correct
1841236454324589 ;3 correct
2659862637316867 ;2 correct
"""
from dataclasses import dataclass
from functools import lru_cache

@dataclass
class Constraint:
    guess: str
    num_correct: int

    @lru_cache(maxsize=None)
    def is_violated(self, guess: str) -> bool:
        num_correct = len([c1 for c1, c2 in zip(guess, self.guess) if c1 == c2])
        if num_correct > self.num_correct or (self.num_correct - num_correct > len(self.guess) - len(guess)):
            return True
        return False
    
    def __hash__(self) -> int:
        return hash((self.guess, self.num_correct))


def load_input(raw: str) -> tuple[Constraint]:
    res = []
    for line in raw.strip().splitlines():
        guess, rest = line.split(' ;')
        num_correct = int(rest.split()[0])
        res.append(Constraint(guess, num_correct))
    res.sort(key=lambda c: c.num_correct)
    return tuple(res)

@lru_cache(maxsize=None)
def could_be_valid(constraints: tuple[Constraint], guess: str) -> bool:
    for constraint in constraints:
        if constraint.is_violated(guess):
            return False
    return True

from collections import deque
def guess(constraints: tuple[Constraint], digits: int) -> str | None:
    queue = deque()
    queue.append("")
    max_seen = 0
    invalid = set()
    while queue:
        curr = queue.popleft()
        if curr in invalid or curr[:-1] in invalid or curr[:-1] in invalid:
            continue
        if len(curr) > max_seen:
            max_seen = len(curr)
            print(len(curr))
        print(curr)
        max_seen = max(max_seen, len(curr))
        if len(curr) == digits and could_be_valid(constraints, curr):
            return curr
        if could_be_valid(constraints, curr):
            for guess in range(0, 10):
                queue.append(curr + str(guess))
        else:
            invalid.add(curr)
    
    
    
assert guess(load_input(test), 5) == "39542"
print(guess(load_input(problem), 16))