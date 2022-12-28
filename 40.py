out = ""
for i in range(1_000_000):
    out += str(i)
    if len(out) >= 1_000_001:
        break
def product(l: list[int]) -> int:
    accumulator = 1
    for n in l:
        accumulator *= n
    return accumulator

print(product(int(out[10 ** i]) for i in range(7)))

