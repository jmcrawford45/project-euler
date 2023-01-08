num = 1777
curr = 1
prev = num
for _ in range(num-1):
    curr = pow(num, prev, 10**8)
    prev = curr
print(curr)
