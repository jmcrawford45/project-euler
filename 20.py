accumulator = 1
for i in range(1, 101):
    accumulator *= i
print(sum(int(c) for c in str(accumulator)))