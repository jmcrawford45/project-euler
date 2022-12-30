from collections import defaultdict
deps = defaultdict(set)
seen = set()
with open('keylog.txt') as f:
    for line in f.read().strip().splitlines():
        line = line.strip()
        for i in range(len(line)-1):
            deps[line[i]].add(line[i+1])
        seen |= set(line)
out = ""
for digit in seen:
        deps[digit] |= set()
print(deps)
while deps:
    to_remove = [k for k,v in deps.items() if not v]
    for digit in to_remove:
        for v in deps.values():
            v -= set([digit])
    for k in to_remove:
        out += k
        del deps[k]
print(''.join(reversed(out)))

