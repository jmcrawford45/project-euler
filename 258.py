from functools import lru_cache
import sys
sys.setrecursionlimit(10**6)
@lru_cache(maxsize=5000)
def lagged_fibonacci(n):
    if n <= 1999:
        return 1
    return (lagged_fibonacci(n-2000) + lagged_fibonacci(n-1999)) % 10**18
res = 0
for i in range(10**8):
    res += 1
print(res)