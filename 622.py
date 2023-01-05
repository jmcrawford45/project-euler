def s(n) -> int:
    if n == 2:
        return 1
    if n == 4:
        return 2
    if n == 6:
        return 4
    if n == 8:
        return 3
    if n == 10:
        return 6

def rifle(l: list[int]) -> list[int]:
    size = len(l)
    l += [0] * len(l)
    for i, e in enumerate(l[:size]):
        if l.index(e) < size // 2:  # first half
            l[size+2*i+1] = e
        else:
            second_half_pos = i-size//2
            l[size + 2*(second_half_pos)] = e
    return l[size:]

def sum_under(target) -> int:     
    res = 0
    for x in range(2, 100, 2):
        count = 0
        l = list(range(x))
        while True:
            l = rifle(l)
            count += 1
            if sorted(l) == l:
                break
        print(x, count, bin(x//2), bin((x+2)//2))
    return res
print(sum_under(60))
