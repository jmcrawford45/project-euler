from functools import lru_cache
@lru_cache(maxsize=None)
def s_number(n: int, target: int) -> bool:
    if n < target or target < 0:
        return False
    if n == target:
        return True
    if len(str(n)) == 1:
        return False
    for i in range(1, len(str(n))):
        start = int(str(n)[:i])
        if s_number(int(str(n)[i:]), target - start):
            return True
    return False
res = 0
for i in range(4, 10**2+1):
    if i % 10**4 == 0:
        print('1k')
    if s_number(i**2, i):
        res += i**2
print(res)
