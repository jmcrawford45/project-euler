with open('triangle.txt') as f:
    raw = f.read()
class Node:
    def __init__(self, val, row, col):
        self.val = val
        self.row = row
        self.col = col
        self.children = []
    def __hash__(self) -> int:
        return hash((self.val, self.row, self.col))
        

pyramid = []
for line in raw.strip().splitlines():
    line = line.strip()
    row = [Node(int(c), len(pyramid), i) for i, c in enumerate(line.split())]
    pyramid.append(row)
for row, nodes in enumerate(pyramid[:-1]):
    for col, node in enumerate(nodes):
        node.children = [pyramid[row+1][col], pyramid[row+1][col+1]]

from functools import lru_cache
@lru_cache(maxsize=None)
def max_path(node: Node) -> int:
    if not node.children:
        return node.val
    return max(node.val + max_path(child) for child in node.children)
print(max_path(pyramid[0][0]))