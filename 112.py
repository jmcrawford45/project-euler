def is_bouncy(n: int) -> bool:
    increasing = int(''.join(sorted(str(n)))) == n
    decreasing = int(''.join(sorted(str(n), reverse=True))) == n
    return not increasing and not decreasing
curr = 1
count_bouncy = 0

while count_bouncy / curr != 0.99:
    if curr % 10000 == 0:
        print(count_bouncy / curr)
    curr += 1
    if is_bouncy(curr):
        count_bouncy += 1
print(curr)