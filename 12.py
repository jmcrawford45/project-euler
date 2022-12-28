from math import *
def num_divisors(n: int) -> int:
    divisors = set()
    for i in range(1, ceil(sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n / i)
    return len(divisors)

curr = 1
term_num = 2
while True:
    curr += term_num
    term_num += 1
    if num_divisors(curr) > 500:
        print(curr)
        break