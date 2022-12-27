from math import sqrt, ceil

def largest_prime_factor(n: int) -> int:
    if n == 1:
        return 1
    for i in reversed(range((ceil(sqrt(n))))):
        if n % i == 0 and largest_prime_factor(i) == 1:
            return i

print(largest_prime_factor(600851475143))