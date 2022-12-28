with open("names.txt") as f:
    names = sorted([n.strip('"').lower() for n in f.read().split(",")])
score_sum = sum((i+1) * sum(ord(c) - ord('a') + 1 for c in name) for i, name in enumerate(names))
print(score_sum)
