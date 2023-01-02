from utils import *
def f(n):
    count = 0
    primes = primes_in_range(2, n+1)
    for i, p1 in enumerate(primes):
        if p1**4 > n:
            break
        for j, p2 in enumerate(primes[i:]):
            if p1*(p2**3) > n:
                break
            for k, p3 in enumerate(primes[j:]):
                if p1*p2*(p3**2) > n:
                    break
                for l, p4 in enumerate(primes[k:]):
                    if p1*p2*p3*p4 > n:
                        break
                    if p1*p2*p3*p4 == n:
                        print(p1,p2,p3,p4)
                        count += 1 
    return count

print(f(100)) 

