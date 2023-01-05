import sys
sys.setrecursionlimit(10**6)
board = []
boards = []
with open('sudoku.txt') as f:
    raw = f.read().strip().splitlines()
from copy import deepcopy
class Board:
    def __init__(self, grid: list[list[int]]) -> None:
        self.grid = grid
        possibilities = []
        for row in grid:
            possibilities_row = []
            for col in row:
                if col == 0:
                    possibilities_row.append(set(range(1, 10)))
                else:
                    possibilities_row.append({col})
            possibilities.append(possibilities_row)
        self.possibilities = possibilities
    
    def _gen_box(self, box_num: int) -> list[tuple[int, int]]:
        row_range = [(box_num // 3) * 3 + i for i in range(3)]
        col_range = [(box_num % 3) * 3 + i for i in range(3)]
        res = []
        for row in row_range:
            for col in col_range:
                res.append((row, col))
        return res
    
    def update_grid(self) -> int:
        changed = 0
        for i, row in enumerate(self.possibilities):
            for j, p in enumerate(row):
                if len(p) == 1 and self.grid[i][j] == 0:
                    changed += 1
                    self.grid[i][j] = list(p)[0]
                elif not p:
                    return -1
        return changed

    
    def update_possibilities(self) -> int:
        for i, row in enumerate(self.grid):
            for j, p in enumerate(self.possibilities[i]):
                if len(p) > 1:
                    p -= set(row)
        for col_num in range(9):
            col = [self.grid[i][col_num] for i in range(9)]
            p_col = [self.possibilities[i][col_num] for i in range(9)]
            for j, p in enumerate(p_col):
                if len(p) > 1:
                    p -= set(col)
        for box_num in range(9):
            box = [self.grid[row][col] for row, col in self._gen_box(box_num)]
            p_box = [self.possibilities[row][col] for row, col in self._gen_box(box_num)]
            for j, p in enumerate(p_box):
                if len(p) > 1:
                    p -= set(box)
        changed = self.update_grid()
        # print(f"solved {changed} squares")
        return changed
    
    def solved(self) ->  bool:
        for row in self.grid:
            if set(row) != set(range(1,10)):
                return False
        for col_num in range(9):
            col = [self.grid[i][col_num] for i in range(9)]
            if set(col) != set(range(1,10)):
                return False
        for box_num in range(9):
            box = [self.grid[row][col] for row, col in self._gen_box(box_num)]
            if set(box) != set(range(1,10)):
                return False
        return True
    
    def guess_square(self, i: int, j: int, v: int):
        for col in range(9):
            self.possibilities[i][col] -= set([v])
        for row in range(9):
            self.possibilities[row][j] -= set([v])
        box_num = (i // 3)*3 + (j // 3)
        for row, col in self._gen_box(box_num):
            self.possibilities[row][col] -= set([v])
        self.possibilities[i][j] = set([v])

    
    def guess(self) -> int:
        res = 0
        while True:
            changed = self.update_possibilities()
            if changed == -1:
                return -1
            elif changed == 0:
                break
            res += changed
        for i in range(len(self.possibilities)):
            row = self.possibilities[i]
            for j in range(len(row)):
                p = row[j]
                tmp_grid = deepcopy(self.grid)
                tmp_possibilities = deepcopy(self.possibilities)
                if len(p) > 1:
                    to_check = list(p)
                    for v in to_check:
                        self.guess_square(i, j, v)
                        changed = self.guess()
                        if changed != -1:
                            res += changed
                            break
                        else:
                            self.possibilities = deepcopy(tmp_possibilities)
                            self.grid = deepcopy(tmp_grid)
                    if changed == -1:
                        return -1
        # if changed and not self.solved():
        #     return -1
        return res
    
    def grid_str(self) -> str:
        return "\n".join("".join([str(c) for c in row]) for row in self.grid)







for line in raw:
    if "grid" in line.lower():
        if board:
            boards.append(Board(board))
            board = []
        continue
    board.append([int(c) for c in line.strip()])
if board:
    boards.append(Board(board))
assert len(boards) == 50     
for board in boards:
    while board.update_possibilities():
        pass
    while board.guess():
        pass
    assert board.update_possibilities() != -1
    print(board.grid_str())
    if not board.solved():
        print('bad')
    print(int(''.join(str(c) for c in board.grid[0][:3])))
res = 0
for board in boards:
    res += int(''.join(str(c) for c in board.grid[0][:3]))
    assert all(board.grid[0][:3])
print(res)
