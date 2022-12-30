field_size = 10 ** 10
curr = 1
for _ in range(1, 7830458):
    curr *= 2
    curr %= field_size
curr *= 28433
curr += 1
print(str(curr)[-10:])