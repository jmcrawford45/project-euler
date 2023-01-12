from math import *
res = 0
squares = [i**2 for i in range(1, 10_000)]
for d in range(2, 1001):
    if floor(sqrt(d)) == sqrt(d):
        continue
    for square in squares:
        if square * d + 1 in squares:
            print(d, sqrt(square * d + 1))
            res += sqrt(square * d + 1)
            break
print(res)