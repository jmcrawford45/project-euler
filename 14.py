from functools import lru_cache

@lru_cache(maxsize=None)
def collatz(n: int) -> int:
    if n == 1:
        return 1
    if n % 2 == 0:
        return 1 + collatz(n//2)
    else:
        return 1 + collatz(3 * n + 1)

res = 0
max_chain = 0
for i in range(1, 1_000_000):
    if collatz(i) > max_chain:
        max_chain = collatz(i)
        res = i
print(res)
