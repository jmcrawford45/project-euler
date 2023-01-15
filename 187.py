def prime_products_below(high: int) -> int:
    sieve = [0] * (high + 1)
    out = set()
    for num, i in enumerate(sieve):
        if num < 2 or i > 0:
            continue
        else:
            sieve[num] = 1
            for multiple in range(num, high, num):
                sieve[multiple] = sieve[multiple//num] + 1
                if sieve[multiple] == 2:
                    out.add(multiple)
    return len([i for i, num in enumerate(sieve) if num == 2])
assert prime_products_below(30) == 10
print(prime_products_below(10**8))
