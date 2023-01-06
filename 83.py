import sys
sys.setrecursionlimit(10**6)
with open('matrix.txt') as f:
    matrix = [[int(c) for c in line.strip().split(",")] for line in f.read().strip().splitlines()]

assert len(matrix) == len(matrix[0])

test_matrix = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]
# matrix = test_matrix
target_col = len(matrix[-1]) - 1
target_row = len(matrix) - 1

def visited(row: int, col: int, prev: int) -> bool:
    return bool(bitmask(row, col) & prev)

def bitmask(row: int, col: int) -> int:
    return 2 ** (row*len(matrix)+col)
# @lru_cache(maxsize=None)
# def min_cost(row: int, col: int, prev: int):
#     if (row, col) == (target_row, target_col):
#         return matrix[row][col]
#     min_from_here = float('inf')
#     if row < len(matrix) - 1 and not visited(row + 1, col, prev):
#         min_from_here = min(min_from_here, matrix[row][col] + min_cost(row+1, col, bitmask(row, col) | prev))
#     if row > 0  and not visited(row - 1, col, prev):
#         min_from_here = min(min_from_here, matrix[row][col] + min_cost(row-1, col, bitmask(row, col) | prev))
#     if col < target_col  and not visited(row, col + 1, prev):
#         min_from_here = min(min_from_here, matrix[row][col] + min_cost(row, col+1, bitmask(row, col) | prev))
#     if col > 0  and not visited(row, col - 1, prev):
#         min_from_here = min(min_from_here, matrix[row][col] + min_cost(row, col-1, bitmask(row, col) | prev))
#     return min_from_here
from collections import deque, defaultdict
def min_cost(row, col):
    queue = deque()
    min_cost = defaultdict(lambda: float('inf'))
    min_cost[0,0] = 0
    queue.append((row, col, 0))
    while queue:
        # print(queue)
        row, col, cost = queue.popleft()
        if cost > min_cost[(row, col)]:
            continue
        for d_row, d_col in [(-1, 0), (1, 0), (0,-1), (0,1)]:
            row2, col2 = row+d_row, col+d_col
            if cost + matrix[row][col] < min_cost[(row2, col2)] and 0 <= row2 < len(matrix) and 0 <= col2 < len(matrix[0]):
                min_cost[row2,col2] = cost + matrix[row][col]
                queue = deque([e for e in queue if e[:2] != (row2, col2)])
                queue.append((row2, col2, min_cost[row2,col2]))
            # elif cost > min_cost[(row2, col2)]:
            #     print(f'skip {row2, col2} with cost {cost}')
    return min_cost[target_row, target_col] + matrix[target_row][target_col]

    

# 1, 2, 
print(min_cost(0, 0))

