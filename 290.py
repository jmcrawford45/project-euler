# idea: maybe sum of digits considering carry separate will be equal mod 10
def normal_sum_product_digits(n, multiplier = 137):
    return sum(int(c) for c in str(multiplier*n))

for i in range(1, 10**3):
    if normal_sum_product_digits(i) % 9 == 0 and normal_sum_product_digits(i) == normal_sum_product_digits(i*137):
        print(i, normal_sum_product_digits(i))