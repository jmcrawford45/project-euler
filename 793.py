from functools import lru_cache

@lru_cache(maxsize=None)
def S(n):
    if n == 0:
        return 290797
    return (S(n-1) ** 2) % 50515093

def M(n):
    prods = [S(j-1)*S(j) % 50515093 for j in range(1, n)]
    print(prods)
    prods.sort()
    print(prods)
    return prods[len(prods)//2]
print(M(4))
assert M(4) == 3878983057768