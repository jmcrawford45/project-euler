from math import factorial
digits = list(str(c) for c in range(10))
target = 1_000_000
out = ""
index = 0
while digits:
    if len(digits) == 2:
        out += ''.join(digits if target == 0 else reversed(digits))
        break
    while factorial(len(digits) - 1) >= target:
        out += str(digits[index])
        del digits[index]
    index = 0
    while target > factorial(len(digits) - 1):
        target -= factorial(len(digits) - 1)
        index += 1
print(out)