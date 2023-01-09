from utils import *
from collections import defaultdict

def min_resilience(target: float) -> int:
    horizon = 10
    while True:
        print(horizon)
        phi = list(range(horizon+1))
        for i, v in enumerate(phi):
            if i < 2:
                continue
            if i == v:
                for j in range(i, len(phi), i):
                    phi[j] //= i
                    phi[j] *= i-1
        for i, p in enumerate(phi):
            if i > 2 and p/(i-1) < target:
                return i
        horizon *= 10
assert min_resilience(4/10) == 12
print(min_resilience(15499/94744))
