from math import *
curr = 1
squares = []
while curr ** 2 < 10**14:
    squares.append(curr ** 2)
    curr += 1

def find_search_start(squares: list[int], n: int) -> int:
    high = len(squares) - 1
    low = 0
    while low < high:
        mid = (high - low) // 2
        if squares[mid] == n:
            return mid
        elif squares[mid] < n:
            low = mid + 1 
        else:
            high = mid - 1
    return high
        


def g(n) -> int:
    end = find_search_start(squares, n)
    for d in reversed(squares[:end]):
        if (n) % d == 0:
            return (d % 1_000_000_007)

def s(n):
    return sum(g(i) for i in range(1, n+1))
assert g(18) == 9
assert s(10) == 24