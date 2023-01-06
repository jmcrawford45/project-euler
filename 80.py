# note: we could technically trivially solve
# by setting decimal precision to 100 manually
# but this allows me to implement the long division
# method from https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Digit-by-digit_calculation

def sqrt(n, num_digits: int = 100):
    """note: n must be natural num < 100"""
    res = 0
    remainder = n
    while len(str(res)) < num_digits and remainder:
        x = 0
        while True:
            if x * (20 * res + x) > remainder:
                x -= 1
                break
            x += 1
        remainder -= x * (20 * res + x)
        # since it's natural, next digits will always be 00 
        remainder *= 100 
        res = 10 * res + x

    return res
res = 0
for i in range(100):
    curr = sqrt(i)
    if len(str(curr)) == 100:
        res += sum(int(c) for c in str(curr))
print(res)
