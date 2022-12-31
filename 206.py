from math import floor, sqrt
target = 1020304050607080900
curr = floor(sqrt(target))
while curr % 10 != 0:
    # end in 0 -> sqrt divisible by 10
    curr += 1
while True:
    if curr % 131110 == 0:
        print(curr**2, str(curr**2)[::2])
    if len(str(curr**2)) == len(str(target)) and str(curr**2)[::2] == "1234567890":
        print(curr)
        break
    curr += 10