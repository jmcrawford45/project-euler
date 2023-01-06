"""
Idea: repeatedly get derivative using slopes.

For k=2, get slope between 2 points. Slope must be linear coefficient and add constant to match series
For k=3
    1,8,27
    7,19
    12 / (k-1) => 6n^2
    subtract values from observed 
    1,8,27
    -5,-16,-27
    repeat for k=2
    slope must be -11
    subtract toget
    6,6,6

    1,8,27,64
    7,19,37
    12,18
    6
"""
from copy import deepcopy
from math import factorial

def optimal_polynomial_next(points: list[int]) -> int:
    """interpolate the n points with a degree n-1 polynomial
    and return value at n+1
    """
    curr = deepcopy(points)
    coefficients = []
    while len(curr) > 1:
        prev_curr = curr
        while len(curr) > 1:
            slopes = []
            for i in range(len(curr) - 1):
                slopes.append(curr[i+1] - curr[i])
            curr = slopes
        coefficients.append(curr[0]//factorial(len(points)-1-len(coefficients)))
        curr = [p-coefficients[-1]*(i+1)**(len(points)-len(coefficients)) for i,p in enumerate(prev_curr)][:-1]
    coefficients.append(curr[0])
    res = 0
    for i, c in enumerate(coefficients):
        res += c*(len(points)+1)**(len(points)-1-i)
    return res

def u(n):
    return 1-n+n**2-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10


assert optimal_polynomial_next([1]) == 1
assert optimal_polynomial_next([1, 8, 27]) == 58
assert optimal_polynomial_next([1, 8]) == 15
res = 0
points = [u(1)]
while len(points) <= 10:
    res += optimal_polynomial_next(points)
    points.append(u(len(points)+1))
print(res)
