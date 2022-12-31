prev_prev_tail = prev_prev_head = 1
prev_tail = prev_head = 1

def pandital_tail(n) -> bool:
    return set(str(n)[-9:]) == set("123456789")

def pandital_head(n) -> bool:
    return set(str(n)[:9]) == set("123456789")

k = 3
while True:
    tail = (prev_prev_tail + prev_tail) % 10**9
    head = int(str(prev_prev_head + prev_head)[:20])
    if len(str(prev_prev_head + prev_head)) == 21:
        prev_head //= 10
    if pandital_head(head) and pandital_tail(tail):
        print(k)
        break
    k += 1
    prev_prev_head = prev_head
    prev_prev_tail = prev_tail
    prev_tail = tail
    prev_head = head