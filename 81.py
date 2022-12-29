with open('matrix.txt') as f:
    matrix = [[int(c) for c in line.strip().split(",")] for line in f.read().strip().splitlines()]

assert len(matrix) == 80
assert len(matrix[0]) == 80
target_row, target_col = len(matrix) - 1, len(matrix[-1]) - 1

from functools import lru_cache

@lru_cache(maxsize=None)
def min_cost(row: int, col: int):
    if (row, col) == (target_row, target_col):
        return matrix[target_row][target_col]
    min_from_here = float('inf')
    if row < target_row:
        min_from_here = min(min_from_here, matrix[row][col] + min_cost(row+1, col))
    if col < target_col:
        min_from_here = min(min_from_here, matrix[row][col] + min_cost(row, col+1))
    return min_from_here

print(min_cost(0,0))

