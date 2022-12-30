def num_rects(max_l: int, max_w: int) -> int:
    res = 0
    for l in range(1, max_l+1):
        for w in range(1, max_w+1):
            res += ((max_l - l) + 1) * ((max_w - w)+1)
    return res
assert num_rects(3,2) == 18
curr_l = 1
closest_dist = float('inf')
closest = (3,2)
while num_rects(curr_l, 1) < 2_000_000:
    for w in range(1, curr_l+1):
        num = num_rects(curr_l, w)
        if abs(2_000_000 - num) < closest_dist:
            print(abs(2_000_000 - num))
            print(curr_l, w)
            closest_dist = abs(2_000_000 - num)
            closest = (curr_l, w)
    curr_l += 1
print(closest[0] * closest[1])

