from utils import *

def prime_prefixes(x: int) -> set[int]:
    res = set()
    for end in range(1, len(str(x))):
        if is_prime(int(str(x)[:end])):
            res.add(int(str(x)[:end]))
    return res

def reverse_digits(x: int) -> int:
    return int(''.join(reversed(str(x))))

def prime_suffixes(x: int) -> set[int]:
    reversed = prime_prefixes(reverse_digits(x))
    return set(reverse_digits(prefix) for prefix in reversed)


digits = 1
found = set()
while not found:
    primes = primes_in_range(max(2, 10**(digits-1)), 10**digits)
    for i, p in enumerate(primes):
        for p2 in primes[i+1:]:
            
        
    digits += 1
print(found)
print(min(found))


