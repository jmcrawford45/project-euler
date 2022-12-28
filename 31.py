from functools import lru_cache

coins = [1,2,5,10,20,50,100,200]

@lru_cache(maxsize=None)
def combos(amount: int, max_usable=coins[-1]) -> int:
    if amount == 0:
        return 1
    if amount < 0:
        return 0
    return sum(combos(amount-coin, coin) for coin in coins if coin <= max_usable)
print(combos(200))