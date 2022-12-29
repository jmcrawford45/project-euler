from math import factorial
res = 0
for i in range(10, 7*factorial(9)):
    if sum(factorial(int(c)) for c in str(i)) == i:
        res += i
print(res)
