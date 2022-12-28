from functools import lru_cache
@lru_cache
def fibonacci(n: int) -> int:
    if n <= 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
curr = 2
while len(str(fibonacci(curr))) < 1000:
    curr += 1
print(curr)