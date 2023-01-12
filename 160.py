"""
idea: since we only need to keep track of last 5 digits, we can compute factorial
of all < 6 digit numbers (99,999!) and raise it to 10**7 to get 10*12! % 10**6
"""
res = 1
for i in range(1, 10**2):
    res *= i
    while res % 10 == 0:
        res //= 10
    res %= 10**2
final_res = res
for i in range(1, 20):
    curr = 1
    for _ in range(100):
        curr *= i
        while curr % 10 == 0:
            curr //= 10
    curr %= 10**2
    final_res *= (curr * res) + res

print(res)
print(final_res)
print(pow(res, 20, 10**4))