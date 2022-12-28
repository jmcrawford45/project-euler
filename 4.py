out = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        if int(''.join(reversed(str(i*j)))) == i * j:
            out = max(out, i*j)
print(out)