from functools import lru_cache

@lru_cache(maxsize=None)
def count_combos(cell: tuple[int, int], targets):
    if cell == (3,3) and set(targets) == set([0]):
        return 1
    if cell == (3,3):
        return 0
    rows = list(targets[:4])
    cols = list(targets[4:8])
    diagonals = list(targets[-2:])
    row, col = cell 
    next_cell = (row, col + 1)
    if next_cell[1] == 4:
        next_cell = (row + 1, 0)
    res = 0
    for i in range(0, 10):
        if rows[row] < i or cols[col] < i:
            continue
        if row == col and diagonals[0] < i:
            continue
        if row == -col and diagonals[1] < i:
            continue
        rows[row] -= i
        cols[col] -= i
        if row == col:
            diagonals[0] -= i
        if row == -col:
            diagonals[1] -= i
        res += count_combos(next_cell, tuple(rows + cols + diagonals))

    return res
    

res = 0
for i in reversed(range((10))):
    res += count_combos((0,0), (i,) * 10)
# print(count_combos((0,0), (1,) * 10))
# assert count_combos((0,0), (0,) * 10) == 1
print(res)