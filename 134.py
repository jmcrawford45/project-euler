from utils import *
print(primes_in_range(0, 10))
high = 1_000_000
primes = primes_in_range(5, high+1)
curr = high+1
while not is_prime(curr):
    curr += 2
primes.append(curr)
res = 0
for i in range(len(primes)-1):
    next_s = primes[i]
    prefix_offset = 10 ** len(str(primes[i]))
    # need x such that prefix_offset * x = (primes[i+1] - primes[i]) modulo primes[i+1]
    gain_per_x = prefix_offset % primes[i+1]
    remainder = primes[i+1] - primes[i]
    x = (pow(prefix_offset, -1, primes[i+1]) * remainder) % primes[i+1]
    next_s += prefix_offset * x
    # print(primes[i], primes[i+1], next_s)
    res += next_s
print(res)
