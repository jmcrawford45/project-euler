curr = 1
for i in range(3, 1002, 2):
    curr += 2 * (2 * (i * i) - 3 * (i - 1))
print(curr)