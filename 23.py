from math import *
def divisors(n: int) -> set[int]:
    divisors = set()
    for i in range(1, ceil(sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n / i)
    return divisors

abundants = [i for i in range(28123) if sum(divisors(i)) > 2*i]
abundants_set = set(abundants)
res = 0
for i in range(28124):
    found_sum = False
    for j in abundants:
        if j > i:
            break
        elif i-j in abundants_set:
            found_sum = True
            break
    if not found_sum:
        res += i
print(res)





