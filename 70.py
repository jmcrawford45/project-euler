from collections import Counter
def is_permutation(x: int, y: int) -> int:
    return Counter(str(x)) == Counter(str(y))

def min_totient_permutation(d: int) -> int:
    phi = list(range(d+1))
    res = 87109
    min_ratio = 87109 / 79180
    for i, v in enumerate(phi):
        if i < 2:
            continue
        if i == v:
            for j in range(i, len(phi), i):
                phi[j] //= i
                phi[j] *= i-1
    for i in range(2, d+1):
        if i % 100000 == 0:
            print(f"{i//100000}%")
        if is_permutation(i, phi[i]) and i / phi[i] < min_ratio:
            min_ratio = i / phi[i]
            res = i
    return res
print(min_totient_permutation(10_000_000))