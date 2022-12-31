# 2(x^2-x) = y^2 - y ; since sequence of consec products is n^2-n and must reduce to 1/2
# ...
# y = 0.5 * (sqrt(8*x**2-8*x+1)+1)
from math import *
f = lambda x: 0.5 * (sqrt(8*x**2-8*x+1)+1)
for x in range(100):
    curr = f(x)
    print(curr)
x = 7.49 * 10**11
while True:
    curr = f(x)
    if 2*x*(x-1) == int(curr)*(int(curr)-1) and int(curr) > 10**12:
        print(x)
        break
    x += 1

