def gcd(x,y):
    while x != y:
        if x > y:
            x -= y
        else:
            y -= x
    return x

def product(l: list[int]) -> int:
    accumulator = 1
    for n in l:
        accumulator *= n
    return accumulator

cancelling = set()
for num in range(10, 100):
    for denom in range(num, 100):
        if num == denom or str(num)[-1] != str(denom)[0]:
            continue
        cancel_num = str(num)[:-1]
        cancel_denom = str(denom)[1:]
        if int(cancel_denom) == 0:
            continue
        if num / denom == int(cancel_num) / int(cancel_denom):
            cancelling.add((num, denom))
prod_num = product([pair[0] for pair in cancelling])
prod_denom = product([pair[1] for pair in cancelling])
print(prod_denom // gcd(prod_denom, prod_num))
