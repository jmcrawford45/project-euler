from utils import is_palindrome
from math import *

def palindromic_sum_below(n: int) -> int:
    squares = [i**2 for i in range(1, floor(sqrt(n))+1)]
    res = 0
    window = 2
    seen = set()
    while window < len(squares):
        for i in range(len(squares)):
            if sum(squares[i:window+i]) >= n:
                break
            if sum(squares[i:window+i]) not in seen and is_palindrome(sum(squares[i:window+i])):
                res += sum(squares[i:window+i])
                seen.add(sum(squares[i:window+i]))
        window += 1
    return res
assert palindromic_sum_below(1000) == 4164
print(palindromic_sum_below(10**8))
