import sys
sys.setrecursionlimit(10**6)
with open('matrix.txt') as f:
    matrix = [[int(c) for c in line.strip().split(",")] for line in f.read().strip().splitlines()]

assert len(matrix) == len(matrix[0])
target_col = len(matrix[-1]) - 1

from functools import lru_cache

@lru_cache(maxsize=None)
def min_cost(row: int, col: int, prev: tuple[int, int]):
    if col == target_col:
        return matrix[row][target_col]
    min_from_here = float('inf')
    if row < len(matrix) - 1 and (row + 1, col) != prev:
        min_from_here = min(min_from_here, matrix[row][col] + min_cost(row+1, col, (row, col)))
    if row > 0 and (row - 1, col) != prev:
        min_from_here = min(min_from_here, matrix[row][col] + min_cost(row-1, col, (row, col)))
    if col < target_col:
        min_from_here = min(min_from_here, matrix[row][col] + min_cost(row, col+1, (row, col)))
    return min_from_here

print(min(min_cost(i,0, (-1, 0)) for i in range(len(matrix))))

