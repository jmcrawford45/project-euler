from functools import lru_cache

@lru_cache(maxsize=None)
def s(k):
    if k in range(1, 56):
        return (100003 - 200003*k + 300007*k**3) % 1000000 - 500000
    return (s(k-24) + s(k-55) + 1000000) % 1000000 - 500000

assert s(10) == -393027
assert s(100) == 86613

def max_subsequence(l) -> int:
    """Using two pointer strategy."""
    res = 0
    left = right = 0
    while left < len(l):
        curr = 0
        while left < len(l) and l[left] <= 0:
            left = right = left + 1
        while right < len(l) and curr >= 0:
            curr += l[right]
            right += 1
            res = max(res, curr)
        left = right
    return res

def _gen_diagonal(start_row: int, start_col: int, d_row: int, d_col: int, grid: list[list[int]]) -> list[int]:
    res = []
    row, col = start_row, start_col
    while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
        res.append(grid[row][col])
        row += d_row
        col += d_col
    return res

test_grid = [
    [-2, 5, 3, 2],
    [9, -6, 5, 1],
    [3, 2, 7, 3],
    [-1, 8, -4, 8],
]


def max_grid_subsequence(grid: list[list[int]]) -> int:
    res = 0
    for row in grid:
        res = max(res, max_subsequence(row))
    for col_num in range(len(grid)):
        col = [grid[i][col_num] for i in range(len(grid))]
        res = max(res, max_subsequence(col))
    for i in range(len(grid)):
        diagonal = _gen_diagonal(0, i, 1, -1, grid)
        diagonal_2 = _gen_diagonal(i, len(grid)-1, 1, -1, grid)
        diagonal_3 = _gen_diagonal(i, 0, -1, 1, grid)
        diagonal_4 = _gen_diagonal(len(grid)-1, i, -1, 1, grid)
        res = max(res, max_subsequence(diagonal), max_subsequence(diagonal_2))
        res = max(res, max_subsequence(diagonal_3), max_subsequence(diagonal_4))
    return res

assert max_grid_subsequence(test_grid) == 16
table = []
for row in range(2000):
    next_row = []
    for col in range(2000):
        next_row.append(s(row*2000+col+1))
    table.append(next_row)
assert len(table) == 2000
assert len(table[0]) == 2000
print(max_grid_subsequence(table))