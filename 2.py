from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    return fibonacci(n-1) + fibonacci(n-2)

out = 0
n = 0
while fibonacci(n) < 4_000_000:
    if fibonacci(n) % 2 == 0:
        out += fibonacci(n)
    n += 1
print(out)