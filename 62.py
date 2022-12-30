from collections import *
counts = defaultdict(set)
curr = 1
while True:
    cube = curr ** 3
    counter = tuple(sorted(Counter(str(cube)).items()))
    counts[counter].add(cube)
    if len(counts[counter]) == 5:
        print(min(counts[counter]))
        break
    curr += 1
