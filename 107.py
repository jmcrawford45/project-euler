from copy import deepcopy
from queue import deque
def load_network(raw: str) -> list[list[int|None]]:
    res = []
    for line in raw.strip().splitlines():
        line = line.strip()
        row = []
        for v in line.split(','):
            if v == '-':
                row.append(None)
            else:
                row.append(int(v))
        res.append(row)
    return res

def cost(network: list[list[int | None]]) -> int:
    res = 0
    for row in network:
        for val in row:
            if val is not None:
                res += val
    return res // 2

def connected(network: list[list[int | None]]) -> bool:
    seen = set()
    bfs = deque()
    bfs.append(0)
    while bfs:
        row = bfs.pop()
        seen.add(row)
        for row, val in enumerate(network[row]):
            if val is not None and row not in seen:
                bfs.append(row)
    return len(seen) == len(network)

def has_redundant(network: list[list[int | None]], col: int) -> bool:
    return len([network[i][col] for i in range(len(network)) if network[i][col] is not None]) > 1
        


def prune_redundant_nodes(network: list[list[int | None]]) -> list[list[int | None]]:
    res  = deepcopy(network)
    candidates = []
    for i, row in enumerate(network):
        for j, val in enumerate(row):
            if val != None:
                candidates.append((val, i, j))
    candidates.sort(reverse=True)
    print(candidates)
    for _, i, j in candidates:
        tmp = res[i][j]
        res[i][j] = None
        res[j][i] = None
        if not connected(res):
            res[i][j] = res[j][i] = tmp

    return res
    




test_network = load_network("""
-,16,12,21,-,-,-
16,-,-,17,20,-,-
12,-,-,28,-,31,-
21,17,28,-,18,19,23
-,20,-,18,-,-,11
-,-,31,19,-,-,27
-,-,-,23,11,27,-
""")

assert test_network[0][1] == 16
print(cost(test_network))
assert cost(test_network) == 243
assert connected(test_network)
pruned = prune_redundant_nodes(test_network)
assert connected(pruned)
assert cost(pruned) == 93

with open('network.txt') as f:
    network = load_network(f.read())
print(cost(network) - cost(prune_redundant_nodes(network)))
