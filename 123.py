from utils import primes_in_range
primes = primes_in_range(2, 1_000_000)

for i, p in enumerate(primes):
    remainder = ((pow(p-1, i+1, p**2) + pow(p+1, i+1, p**2))) % p**2
    if remainder > 10**10:
        print(i+1)
        break
